from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
# from posts.forms import LoginForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponse, HttpRequest

def signup(request):
    message = ""
    if request.method == "POST":
        # message = ""
        form = UserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            message += "Sign-up successful!"
        else:
            message += "Sign-up unsuccessful.  Please try again."

    form = UserCreationForm
    context = {
        'form': form, 
        'message':message
        }
    return render(request, 'users/signup.html', context)

# def login(request):
#     user = None
#     form = AuthenticationForm(data = request.POST)
#     if form.is_valid():
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#     if user is not None:
#         login(request, user)
#         return redirect("/posts/world")
#     else:
#         print("Not valid!")
#         return redirect("/")




def user_login(request):
    user = None
    form = AuthenticationForm(data = request.POST)
    if form.is_valid():
        print("form is valid!")
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(request, username=username, password=password)
    # else:
    #     print(form.errors)
    if user != None:
        login(request, user)
        return redirect("/posts/worldextend")
    else:
        print("Not valid!")
        return redirect("/")























###############################
#SCRAP


# Based heavily on Pete's examples on Github

# def login_user(request):
#     context = {}
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('') # might need to fix this... 'posts:home'

# def logout_user(request):
#     logout(request)
#     return redirect('') # double check these... 'posts:home'

# def signup(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password1 = request.POST.get('password1')
#         password2 = request.POST.get('password2')

#         message = ''
#         if password1 != password2:
#             message += "Passwords do not match."

#         if User.objects.filter(username=username).exists():
#             message += "Username already taken."

#         if message:
#             message += "Please try again." # pretty much all pete, good stuff lol
        
#         else:
#             user = User.objects.create_user(username=username, password=password1)
#             login(request, user)
#             return redirect('') # 'posts:home' ?
#     context = {'message': message}
#     return render(request, 'users/signup.html', context)

# def signup(request):
#     message = ""
#     if request.method == "POST":
#         # message = ""
#         form = SignupForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#         # Do I need another return field here??

#     form = SignupForm()    
#     context = {'form': form}
#     return render(request, 'users/signup.html', context)


# def login(request):
#     user = None
#     form = AuthenticationForm(request.POST)
#     if form.is_valid():
#         # print("form is valid!")
#         username = form.cleaned_data['username']
#         password = form.cleaned_data['password']
#         user = authenticate(request, username=username, password=password)
#     # else:
#     #     print(form.errors)
#     if user is not None:
#         login(request, user)
#         return redirect("/posts/world")
#     else:
#         print("Not valid!")
#         return redirect("/")