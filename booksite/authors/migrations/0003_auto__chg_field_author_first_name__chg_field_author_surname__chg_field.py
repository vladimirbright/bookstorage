# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'Author.first_name'
        db.alter_column('authors_author', 'first_name', self.gf('django.db.models.fields.CharField')(max_length=150))

        # Changing field 'Author.surname'
        db.alter_column('authors_author', 'surname', self.gf('django.db.models.fields.CharField')(max_length=150))

        # Changing field 'Author.nickname'
        db.alter_column('authors_author', 'nickname', self.gf('django.db.models.fields.CharField')(max_length=150))

        # Changing field 'Author.second_name'
        db.alter_column('authors_author', 'second_name', self.gf('django.db.models.fields.CharField')(max_length=150))


    def backwards(self, orm):
        
        # Changing field 'Author.first_name'
        db.alter_column('authors_author', 'first_name', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'Author.surname'
        db.alter_column('authors_author', 'surname', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'Author.nickname'
        db.alter_column('authors_author', 'nickname', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'Author.second_name'
        db.alter_column('authors_author', 'second_name', self.gf('django.db.models.fields.CharField')(max_length=50))


    models = {
        'authors.author': {
            'Meta': {'object_name': 'Author'},
            'birth_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'death_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nickname': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'second_name': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        }
    }

    complete_apps = ['authors']
