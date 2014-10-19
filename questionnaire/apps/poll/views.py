# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect,  HttpResponse
from django.core.urlresolvers import reverse
from django.views.generic import ListView, DetailView
from .models import Question, Answer, User


def vote(request, poll_id):

    question = get_object_or_404(Question, pk=poll_id)
    if not question.is_active:
        return HttpResponse(u'Опрос снят с публикации')
    user = User()
    user.ip = user.get_user_ip(request)
    user.question = question
    if user.voted_already():
        return HttpResponse(u'Вы уже голосовали в этом опросе')

    if request.POST.get('answer'):
        try:
            selected_answer = question.answer_set.get(pk=request.POST['answer'])
        except(Answer.DoesNotExist, UnicodeEncodeError, ValueError):
            return render(request, 'poll/detail.html', {
                'question': question,
                'error_message': u"Указан недопустимый ответ"})
        selected_answer.votes += 1
        selected_answer.save()
        user.save()
        return HttpResponseRedirect(reverse('poll:results', args=(question.id,)))
    else:
        return render(request, 'poll/detail.html', {
            'question': question,
            'error_message': u"Вы не выбрали ответ."})

class  IndexView(ListView):
    template_name = 'poll/index.html'
    context_object_name = 'latest_questions_list'

    def get_queryset(self):
        """Вернуть два последних свежих опроса"""
        return Question.objects.order_by('-date_published')[:4]

class PollDetailView(DetailView):
    model = Question
    template_name = 'poll/detail.html'

    def get_context_data(self, **kwargs):
        context = super(PollDetailView, self).get_context_data(**kwargs)
        user = User()
        user.ip = user.get_user_ip(self.request)
        user.question = Question.objects.get(pk=self.kwargs['pk'])
        # Передаем в шаблон переменную
        context['voted_already'] = user.voted_already()
        return context

class ResultsView(DetailView):
    model = Question
    template_name = 'poll/results.html'