from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm 

def register(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        user_obj = form.save()
        return redirect('/posts/index.html')
    context= {'form': form}
    return render (request, 'users/registration.html',context)

def login_view(request):
    if request.method =='POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('posts/index.html')
        else:
            form = AuthenticationForm(request)
        context ={
            'form':form
        }
        return render(request, "users/login.html",context)

def logout(request):
    
    return redirect ('posts/index.html')
        
        
        
        
