from django.contrib import admin

from .models import Authors, Books
# Register your models here.
admin.site.register(Authors)
admin.site.register(Books)
