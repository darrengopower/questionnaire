# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'User'
        db.create_table(u'poll_user', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ip', self.gf('django.db.models.fields.GenericIPAddressField')(max_length=39)),
            ('question', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['poll.Question'])),
        ))
        db.send_create_signal(u'poll', ['User'])


    def backwards(self, orm):
        # Deleting model 'User'
        db.delete_table(u'poll_user')


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
            'date_published': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 10, 19, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'poll.user': {
            'Meta': {'object_name': 'User'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.GenericIPAddressField', [], {'max_length': '39'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['poll.Question']"})
        }
    }

    complete_apps = ['poll']