from django.shortcuts import render
from .models import Book
from .models import Library


# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()  # required: use this exact method
    return render(request, "relationship_app/list_books.html", {'books': books})


# Class-based view for library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"  # required
    context_object_name = "library"  # required
