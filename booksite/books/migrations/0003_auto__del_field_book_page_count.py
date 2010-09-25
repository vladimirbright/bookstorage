# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Book.page_count'
        db.delete_column('books_book', 'page_count')


    def backwards(self, orm):
        
        # Adding field 'Book.page_count'
        db.add_column('books_book', 'page_count', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True), keep_default=False)


    models = {
        'authors.author': {
            'Meta': {'object_name': 'Author'},
            'birth_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'death_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nickname': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'second_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'books.book': {
            'Meta': {'object_name': 'Book'},
            'abstract': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'authors': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['authors.Author']", 'symmetrical': 'False'}),
            'cover': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        }
    }

    complete_apps = ['books']
