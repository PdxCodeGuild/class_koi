from django.contrib import admin

from .models import Author, Book, CheckOut

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(CheckOut)

