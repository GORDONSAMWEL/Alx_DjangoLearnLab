# Define a BookSerializer class that extends rest_framework.serializers.ModelSerializer and includes all fields of the Book model.
from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'