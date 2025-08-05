from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from api.models import Book, Author


class BookAPITestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.author = Author.objects.create(name="John Doe", birth_date="1970-01-01")

        self.book1 = Book.objects.create(
            title="Alpha Book", author=self.author, publication_year=2001
        )
        self.book2 = Book.objects.create(
            title="Beta Book", author=self.author, publication_year=1999
        )

        self.book_list_url = reverse('book-list')
        self.book_detail_url = lambda pk: reverse('book-detail', args=[pk])
        self.book_create_url = reverse('book-create')
        self.book_update_url = lambda pk: reverse('book-update', args=[pk])
        self.book_delete_url = lambda pk: reverse('book-delete', args=[pk])

    def authenticate(self):
        self.client.login(username='testuser', password='testpass')

    # --- CREATE ---
    def test_create_book_authenticated(self):
        self.authenticate()
        data = {
            "title": "New Book",
            "author": self.author.id,
            "publication_year": 2020
        }
        response = self.client.post(self.book_create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_book_unauthenticated(self):
        data = {
            "title": "Fail Book",
            "author": self.author.id,
            "publication_year": 2022
        }
        response = self.client.post(self.book_create_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # --- LIST & DETAIL ---
    def test_list_books(self):
        response = self.client.get(self.book_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_retrieve_book_detail(self):
        response = self.client.get(self.book_detail_url(self.book1.pk))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book1.title)

    # --- UPDATE ---
    def test_update_book_authenticated(self):
        self.authenticate()
        data = {"title": "Updated Book", "author": self.author.id, "publication_year": 2023}
        response = self.client.put(self.book_update_url(self.book1.pk), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Book")

    def test_update_book_unauthenticated(self):
        data = {"title": "Fail Update", "author": self.author.id, "publication_year": 2023}
        response = self.client.put(self.book_update_url(self.book1.pk), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # --- DELETE ---
    def test_delete_book_authenticated(self):
        self.authenticate()
        response = self.client.delete(self.book_delete_url(self.book1.pk))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(pk=self.book1.pk).exists())

    def test_delete_book_unauthenticated(self):
        response = self.client.delete(self.book_delete_url(self.book1.pk))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # --- FILTERING ---
    def test_filter_books_by_author(self):
        response = self.client.get(f"{self.book_list_url}?author={self.author.id}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(all(book["author"] == self.author.id for book in response.data))

    # --- SEARCHING ---
    def test_search_books_by_title(self):
        response = self.client.get(f"{self.book_list_url}?search=Alpha")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Alpha Book")

    # --- ORDERING ---
    def test_order_books_by_publication_year(self):
        response = self.client.get(f"{self.book_list_url}?ordering=publication_year")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["publication_year"], 1999)
