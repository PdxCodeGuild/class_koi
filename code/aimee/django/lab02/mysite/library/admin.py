from django.contrib import admin

from .models import Book, Author, CheckedOut

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(CheckedOut)
