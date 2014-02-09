# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Jurisdiction'
        db.create_table(u'foiaface_jurisdiction', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('contact', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['foiaface.Contact'])),
            ('parent_jurisdiction', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='children', null=True, to=orm['foiaface.Jurisdiction'])),
            ('jurisdiction_type', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'foiaface', ['Jurisdiction'])

        # Adding model 'Contact'
        db.create_table(u'foiaface_contact', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
        ))
        db.send_create_signal(u'foiaface', ['Contact'])

        # Adding model 'Request'
        db.create_table(u'foiaface_request', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('requester_first_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('requester_last_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('requester_email', self.gf('django.db.models.fields.EmailField')(max_length=255)),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'foiaface', ['Request'])

        # Adding M2M table for field jurisdiction on 'Request'
        m2m_table_name = db.shorten_name(u'foiaface_request_jurisdiction')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('request', models.ForeignKey(orm[u'foiaface.request'], null=False)),
            ('jurisdiction', models.ForeignKey(orm[u'foiaface.jurisdiction'], null=False))
        ))
        db.create_unique(m2m_table_name, ['request_id', 'jurisdiction_id'])


    def backwards(self, orm):
        # Deleting model 'Jurisdiction'
        db.delete_table(u'foiaface_jurisdiction')

        # Deleting model 'Contact'
        db.delete_table(u'foiaface_contact')

        # Deleting model 'Request'
        db.delete_table(u'foiaface_request')

        # Removing M2M table for field jurisdiction on 'Request'
        db.delete_table(db.shorten_name(u'foiaface_request_jurisdiction'))


    models = {
        u'foiaface.contact': {
            'Meta': {'object_name': 'Contact'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'foiaface.jurisdiction': {
            'Meta': {'object_name': 'Jurisdiction'},
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['foiaface.Contact']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jurisdiction_type': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'parent_jurisdiction': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': u"orm['foiaface.Jurisdiction']"})
        },
        u'foiaface.request': {
            'Meta': {'object_name': 'Request'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jurisdiction': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['foiaface.Jurisdiction']", 'symmetrical': 'False'}),
            'requester_email': ('django.db.models.fields.EmailField', [], {'max_length': '255'}),
            'requester_first_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'requester_last_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'text': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['foiaface']