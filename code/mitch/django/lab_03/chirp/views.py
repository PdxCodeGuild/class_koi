
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import ChirpPost

def index(request):
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('users:login')
        text = request.POST.get('post_text')
        ChirpPost.objects.create(
            text=text,
            user=request.user
        )
        return redirect('chirp:index')
    
    all_chirps = ChirpPost.objects.order_by("-date_time")
    context = {
        'all_chirps' : all_chirps,
    }
    return render(request, 'chirp/index.html', context)
    
def page_not_found (request, exception):
    return render(request, 'chirp/404.html', status=404)
    
    
    
    
    
    