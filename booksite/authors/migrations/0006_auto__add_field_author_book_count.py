# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Author.book_count'
        db.add_column('authors_author', 'book_count', self.gf('django.db.models.fields.PositiveIntegerField')(default=0), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Author.book_count'
        db.delete_column('authors_author', 'book_count')


    models = {
        'authors.author': {
            'Meta': {'ordering': "('letter',)", 'object_name': 'Author'},
            'birth_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'book_count': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'death_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'letter': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': "orm['authors.FirstLetter']", 'null': 'True'}),
            'nickname': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'second_name': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        'authors.firstletter': {
            'Meta': {'ordering': "('letter',)", 'object_name': 'FirstLetter'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'letter': ('django.db.models.fields.SlugField', [], {'max_length': '5', 'db_index': 'True'})
        }
    }

    complete_apps = ['authors']
