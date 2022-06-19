from django.urls import path
from bookstore.views import *

urlpatterns = [
    path('books/', all_books),
    path('books/<int:book_id>', onde_book),
    path('authors/<int:author_id>', onde_author),
]
