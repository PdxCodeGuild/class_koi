from django.shortcuts import render, redirect

from django.http import HttpResponse

from .models import Books


def index(request):
    if request.method == 'POST':

        name = request.POST.get('name'),
        publish_date = request.get('publish_date')
        author = request.POST.get('author')
        checked_status = request.POST.get('checked_status')
        book_list = Books.objects.create(
            name=name,
            publish_date=publish_date,
            author=author,
            checked_status=checked_status,
        )
        return redirect('library/index.html')
    author = Books.objects.filter('author')
    all_books = Books.objects.all()
    context = {
        'all_books': all_books,
    }
    return render(request, 'library/index.html', context)
