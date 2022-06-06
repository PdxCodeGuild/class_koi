from rest_framework.serializers import ModelSerializer

from library.models import Author, Book

class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__' # this will give all the fields
        # fields = ('first_name', 'last_name') # this will just give whichever fields are provided
    
    # overriding the update method
    def update(self, instance, validated_data):
        print('here is a print statement, but the update still happens like usual')
        # make everything all caps:
        # validated_data['first_name'] = validated_data['first_name'].upper()
        # validated_data['last_name'] = validated_data['last_name'].upper()
        return super().update(instance, validated_data) # this line is saying (go ahead and do what you'd usually do)

class BookSerializer(ModelSerializer):
    author_detail = AuthorSerializer(read_only=True, source='author')
    class Meta:
        model = Book
        fields = '__all__'