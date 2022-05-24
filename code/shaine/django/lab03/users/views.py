from django.shortcuts import render, redirect
from .forms import RegisterForm, ProfileUpdateForm

from django.contrib import messages
from django.contrib.auth.decorators import login_required


def register(request):
    if (request.method == 'POST'):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Account Created')
            return redirect('login')

    else:
        form = RegisterForm()
        return render(request, 'users/register.html',{'form': form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')

def profileupdate(request):
    if(request.method == 'POST'):
        pform = ProfileUpdateForm(request.POST,request.FILES,instance= request.user.profile)
        if pform.is_valid:
            pform.save()
            return redirect('profile')

    else:
        pform = ProfileUpdateForm(instance= request.user.profile)

    return render(request, 'users/profileupdate.html', {'pform': pform})