from django.contrib import admin

from .models import Author, Book, Checkout, Genre

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Checkout)
admin.site.register(Genre)
