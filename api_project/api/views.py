# api/views.py
from rest_framework import generics, viewsets
from .models import Book
from .serializers import BookSerializer
from rest_framework import permissions

# Old list-only view
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

# Full CRUD viewset
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


    """
Authentication & Permissions:
- This API uses DRF's TokenAuthentication.
- Obtain a token via POST to /api-token-auth/ with username & password.
- Include the token in the "Authorization: Token <yourtoken>" header for all requests.
- Only authenticated users can perform CRUD on Book endpoints.
"""

