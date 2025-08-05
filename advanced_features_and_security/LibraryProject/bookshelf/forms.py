from django import forms
from .models import Book  # assuming you have a Book model

class ExampleForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date']  # adjust fields to match your Book model
