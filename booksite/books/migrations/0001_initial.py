# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Book'
        db.create_table('books_book', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('abstract', self.gf('django.db.models.fields.CharField')(max_length=400, blank=True)),
            ('page_count', self.gf('django.db.models.fields.PositiveIntegerField')(blank=True)),
            ('cover', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
        ))
        db.send_create_signal('books', ['Book'])

        # Adding M2M table for field authors on 'Book'
        db.create_table('books_book_authors', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('book', models.ForeignKey(orm['books.book'], null=False)),
            ('author', models.ForeignKey(orm['authors.author'], null=False))
        ))
        db.create_unique('books_book_authors', ['book_id', 'author_id'])


    def backwards(self, orm):
        
        # Deleting model 'Book'
        db.delete_table('books_book')

        # Removing M2M table for field authors on 'Book'
        db.delete_table('books_book_authors')


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
            'page_count': ('django.db.models.fields.PositiveIntegerField', [], {'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        }
    }

    complete_apps = ['books']
