# Lab 04 (Optional): Django Rest Framework Todos

Write a Todo List app in Django with a [Django Rest Framework](https://www.django-rest-framework.org) api and a [Vue](https://v3.vuejs.org) frontend.  

Create 2 apps:
  - `todos`: This app will have your `Todo` model and serve your Vue templates, which will use `axios` or `fetch` to send AJAX requests to your other app...
  - `api`: This app will be built with Django Rest Framework.  Create a `serializers.py` to with a `ModelSerializer` based off your `Todo` model.  In the `views.py`, use `rest_framework.generics` or perhaps another method to serve your API.  (Hint: `generics.ListCreateAPIView` and `generics.RetrieveUpdateDestroyAPIView` provide all of the CRUD functionality needed)

If you need to study up on Django Rest Framework, do their [tutorial](https://www.django-rest-framework.org/tutorial/1-serialization/) first.  Do at least the first 3 parts to have everything you need to complete this lab.