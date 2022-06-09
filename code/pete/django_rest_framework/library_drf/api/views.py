from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from library.models import Author, Book
from .serializers import AuthorSerializer, BookSerializer

# the ListCreateAPIView is for one url endpoint: api/v1/authors/
# if sent a GET request, it a list of all the author objects in the db
# in JSON format
# if sent a POST request (including a dictinoary of data for a new author),
# it will create a new author
class AuthorList(ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    # an axios request like this:
    # axios({
    #   url: '127.0.0.1:8000/api/v1/authors/' 
    #   method: 'post',
    #   data: { first_name: 'John', last_name: 'Grisham' }
    # })
    # will create a new author in the DB


# the RetrieveUpdateDestroyAPIView is used for the api/v1/authors/[author id goes here]/
# given a DELETE request, it will delete the object form the db
# given a PUT request, with form data (or the data object in an axios call),
# it will fully update the object with those values
# given a PATCH request, with form data (or the data object in an axios call) (I think this is the body object in fetch),
# it will update all fields passed in
class AuthorDetail(RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    # delete in axios:
    # axios({
    #   url: '127.0.0.1:8000/api/v1/author/8/'
    #   method: 'delete',
    # }) // this will delete the author with id 8

    # patch({
    #   url: '127.0.0.1:8000/api/v1/author/7/,
    #   method: 'patch',
    #   data: { last_name: 'Bon Jovi' }        
    # }) // this will update the author with id 7 to have the last_name 'Bon Jovi'


class BookList(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetail(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

