# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Question'
        db.create_table(u'poll_question', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('date_published', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 10, 17, 0, 0))),
            ('is_active', self.gf('django.db.models.fields.BooleanField')()),
        ))
        db.send_create_signal(u'poll', ['Question'])

        # Adding model 'Answer'
        db.create_table(u'poll_answer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('question_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['poll.Question'])),
            ('answer', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('votes', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'poll', ['Answer'])


    def backwards(self, orm):
        # Deleting model 'Question'
        db.delete_table(u'poll_question')

        # Deleting model 'Answer'
        db.delete_table(u'poll_answer')


    models = {
        u'poll.answer': {
            'Meta': {'object_name': 'Answer'},
            'answer': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['poll.Question']"}),
            'votes': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'poll.question': {
            'Meta': {'object_name': 'Question'},
            'date_published': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 10, 17, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['poll']