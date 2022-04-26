from django.shortcuts import render
from django.http import HttpResponse

# Create views below
def index(request):
    return HttpResponse("you're home, baby")