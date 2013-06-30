# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Project'
        db.create_table('issues_project', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('creator', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='projects', null=True, to=orm['auth.User'])),
            ('project', self.gf('django.db.models.fields.CharField')(max_length=60)),
        ))
        db.send_create_signal('issues', ['Project'])

        # Adding model 'Tag'
        db.create_table('issues_tag', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('creator', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='tags', null=True, to=orm['auth.User'])),
            ('tag', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal('issues', ['Tag'])

        # Adding model 'Issue'
        db.create_table('issues_issue', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('creator', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='created_issues', null=True, to=orm['auth.User'])),
            ('body', self.gf('django.db.models.fields.TextField')(default='', max_length=3000, blank=True)),
            ('body_html', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='issues', null=True, to=orm['auth.User'])),
            ('priority', self.gf('django.db.models.fields.IntegerField')(default=0, null=True, blank=True)),
            ('difficulty', self.gf('django.db.models.fields.IntegerField')(default=0, null=True, blank=True)),
            ('progress', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('closed', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='issues', null=True, to=orm['issues.Project'])),
        ))
        db.send_create_signal('issues', ['Issue'])

        # Adding M2M table for field tags on 'Issue'
        db.create_table('issues_issue_tags', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('issue', models.ForeignKey(orm['issues.issue'], null=False)),
            ('tag', models.ForeignKey(orm['issues.tag'], null=False))
        ))
        db.create_unique('issues_issue_tags', ['issue_id', 'tag_id'])

        # Adding model 'Comment'
        db.create_table('issues_comment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('creator', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='comments', null=True, to=orm['auth.User'])),
            ('issue', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='comments', null=True, to=orm['issues.Issue'])),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('body', self.gf('django.db.models.fields.TextField')(max_length=3000)),
            ('body_html', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('issues', ['Comment'])


    def backwards(self, orm):
        # Deleting model 'Project'
        db.delete_table('issues_project')

        # Deleting model 'Tag'
        db.delete_table('issues_tag')

        # Deleting model 'Issue'
        db.delete_table('issues_issue')

        # Removing M2M table for field tags on 'Issue'
        db.delete_table('issues_issue_tags')

        # Deleting model 'Comment'
        db.delete_table('issues_comment')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'issues.comment': {
            'Meta': {'object_name': 'Comment'},
            'body': ('django.db.models.fields.TextField', [], {'max_length': '3000'}),
            'body_html': ('django.db.models.fields.TextField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'comments'", 'null': 'True', 'to': "orm['auth.User']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'issue': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'comments'", 'null': 'True', 'to': "orm['issues.Issue']"})
        },
        'issues.issue': {
            'Meta': {'object_name': 'Issue'},
            'body': ('django.db.models.fields.TextField', [], {'default': "''", 'max_length': '3000', 'blank': 'True'}),
            'body_html': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'closed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'created_issues'", 'null': 'True', 'to': "orm['auth.User']"}),
            'difficulty': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'issues'", 'null': 'True', 'to': "orm['auth.User']"}),
            'priority': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'progress': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'issues'", 'null': 'True', 'to': "orm['issues.Project']"}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'issues'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['issues.Tag']"})
        },
        'issues.project': {
            'Meta': {'object_name': 'Project'},
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'projects'", 'null': 'True', 'to': "orm['auth.User']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'project': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        'issues.tag': {
            'Meta': {'object_name': 'Tag'},
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'tags'", 'null': 'True', 'to': "orm['auth.User']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tag': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['issues']