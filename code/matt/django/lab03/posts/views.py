from django.shortcuts import render
from django.http import HttpResponse

def testview(request):
    return HttpResponse('Hello posts world!')