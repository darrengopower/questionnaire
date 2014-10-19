# -*- coding:utf-8 -*-
from django.contrib import admin
from .models import Question, Answer, User

class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 2

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,
            {'fields': ['title', 'is_active']}
        ),
        ('Информация о дате',
            {'fields': ['date_published'],
            'classes': ['collapse']}
        ),
    ]
    inlines = [AnswerInline]
    list_display = ('title', 'date_published', 'is_active', 'is_popular')
    list_filter = ['date_published']
    search_fields = ['title']
    # date_hierarchy = ['date_published']


admin.site.register(Question, QuestionAdmin)

class UserAdmin(admin.ModelAdmin):
    list_display = ('ip', 'question')

admin.site.register(User, UserAdmin)