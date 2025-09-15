# api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet

# Create a router and register the BookViewSet
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Route for the ListAPIView (previous implementation)
    path('books/', BookList.as_view(), name='book-list'),

    # Routes for ViewSet (CRUD operations)
    path('', include(router.urls)),
]
