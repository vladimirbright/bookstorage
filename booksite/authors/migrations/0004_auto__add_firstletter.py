# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'FirstLetter'
        db.create_table('authors_firstletter', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('letter', self.gf('django.db.models.fields.SlugField')(max_length=5, db_index=True)),
        ))
        db.send_create_signal('authors', ['FirstLetter'])


    def backwards(self, orm):
        
        # Deleting model 'FirstLetter'
        db.delete_table('authors_firstletter')


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
        },
        'authors.firstletter': {
            'Meta': {'object_name': 'FirstLetter'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'letter': ('django.db.models.fields.SlugField', [], {'max_length': '5', 'db_index': 'True'})
        }
    }

    complete_apps = ['authors']
