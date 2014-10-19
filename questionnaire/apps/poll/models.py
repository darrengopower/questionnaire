# -*- coding:utf-8 -*-

import datetime
from django.db import models
from poll import poll_settings

class Question(models.Model):
    "Вопрос"""
    title = models.CharField(max_length=200, verbose_name = u"Вопрос")
    date_published = models.DateTimeField(verbose_name = u"Дата публикации",
        default = datetime.datetime.now())
    is_active = models.BooleanField(verbose_name = u"Опубликован")
    def is_popular(self):
        # answers = Answer.objects.filter(question_id=self.id)
        # votes_total = sum([answer.votes for answer in answers])

        # Vados variant with aggregate
        votes_total = Answer.objects.filter(question_id=self.id).aggregate(votes_total=models.Sum('votes'))
        return votes_total['votes_total'] > poll_settings.POLLS_POPULAR_VOTES_LIMIT
    is_popular.short_description = u'Популярный'
    # Замена значений True и False на иконки
    is_popular.boolean = True

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'Вопрос'
        verbose_name_plural = u'Вопросы'


class Answer(models.Model):
    """Вариант ответа на вопрос"""
    question_id = models.ForeignKey(Question)
    answer = models.CharField(max_length=200, verbose_name = u"Ответ")
    votes = models.IntegerField(verbose_name = u"Голос", default = 0)

    def __unicode__(self):
        return self.answer

    class Meta:
        verbose_name = u'Ответ'
        verbose_name_plural = u'Ответы'

class User(models.Model):
    u"""Пользователь, участвующий в опросе"""
    ip = models.GenericIPAddressField(verbose_name=u'IP пользователя')
    question = models.ForeignKey(Question, verbose_name=u'Вопрос голосования')

    def __unicode__(self):
        return self.ip

    def get_user_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[-1].strip()
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    def voted_already(self):
        """Голосовал ли пользователь с данным ip в опросе"""
        user_list = User.objects.filter(ip=self.ip, question = self.question)
        return len(user_list) > 0

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'