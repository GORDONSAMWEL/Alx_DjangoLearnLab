# Define the View:
# In api/views.py, create a view named BookList that extends rest_framework.generics.ListAPIView.
# Use the BookSerializer to serialize the data and the Book model as the queryset.

from rest_framework.generics import ListAPIView
from .serializers import BookSerializer
from .models import Book

class BookList(ListAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()







