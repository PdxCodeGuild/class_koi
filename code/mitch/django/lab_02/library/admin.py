from django.contrib import admin

from .models import Book, Author, Checkout, Genre
# Register your models here.


admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Checkout)
admin.site.register(Genre)