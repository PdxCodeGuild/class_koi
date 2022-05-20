from django.contrib import admin

<<<<<<< Updated upstream
from .models import Authors, Books
=======
from .models import Authors, Books, Checked_Book
>>>>>>> Stashed changes
# Register your models here.
admin.site.register(Authors)
admin.site.register(Books)
admin.site.register(Checked_Book)
