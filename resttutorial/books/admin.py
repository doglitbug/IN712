from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'created' , 'author' ,'intro', 'price', 'url']

admin.site.register(Book, BookAdmin)
