from django.urls import path
from .views import bookAPI, booksAPI

urlpatterns = [
    path("fbv/books/", booksAPI),
    path("fbv/book/<int:bid>/", bookAPI),
]