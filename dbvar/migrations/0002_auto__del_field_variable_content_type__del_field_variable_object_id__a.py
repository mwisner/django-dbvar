# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Variable.content_type'
        db.delete_column('dbvar_variable', 'content_type_id')

        # Deleting field 'Variable.object_id'
        db.delete_column('dbvar_variable', 'object_id')

        # Adding unique constraint on 'Variable', fields ['key']
        db.create_unique('dbvar_variable', ['key'])


    def backwards(self, orm):
        # Removing unique constraint on 'Variable', fields ['key']
        db.delete_unique('dbvar_variable', ['key'])

        # Adding field 'Variable.content_type'
        db.add_column('dbvar_variable', 'content_type',
                      self.gf('django.db.models.fields.related.ForeignKey')(default='', to=orm['contenttypes.ContentType']),
                      keep_default=False)

        # Adding field 'Variable.object_id'
        db.add_column('dbvar_variable', 'object_id',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=''),
                      keep_default=False)


    models = {
        'dbvar.variable': {
            'Meta': {'object_name': 'Variable'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'value': ('jsonfield.fields.JSONField', [], {'default': '{}'})
        }
    }

    complete_apps = ['dbvar']