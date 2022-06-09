from django.shortcuts import render
from django.http import JsonResponse

import json

from .models import ToDo

def index(request):
    return render(request, 'vue_todos/index.html')

def get_todos(request):
    todos_db = ToDo.objects.all() # get all the todos from the db
    todos = [] # create a list to be sent in the JsonResponse
    for todo in todos_db: # add a dictionary version of each todo
        # to the list to be sent to the frontend
        todos.append({
            'text': todo.text,
            'completed': todo.completed
        })
    # the reason that a list, instead of a QuerySet, is being
    # passed into the JsonResponse... is that a QuerySet is not
    # json-serializable... only the most primitive datatypes
    # are json-serializable: strings, integers, floats, booleans, lists, dictionaries, None
    return JsonResponse(data={'todos': todos})

def add_todo(request):
    if request.method == 'POST': # only attempt todo creation on post requests
        # print(json.loads(request.body))
        data = json.loads(request.body) # request.body is a JSON-formatted string of what was passed
        # in the data object of the axios call on the frontend
        text = data.get('text') # data['text'] would also work, but would raise a
        # KeyError if there was no 'text' key in the dictionary
        ToDo.objects.create(text=text) # create a new todo object w/ that text
        return JsonResponse({'message': 'ok'})
    # return json response without altering db otherwise
    return JsonResponse({'message': 'post requests only 😜'})