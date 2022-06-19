from curses.ascii import isdigit
from django.http import HttpResponseNotFound, HttpResponse
from django.shortcuts import render
from bookstore.mock_data import BOOKS, AUTHORS


def all_books(request):
    books = BOOKS
    author_param = request.GET.get('author')

    if author_param and isdigit(author_param):
        author_id = int(author_param)
        books = [book for book in BOOKS if book['author_id'] == author_id]

    return render(request, 'bookstore/books_lis.html', context={
        'books': books,
        'has_author_param': bool(author_param)
    })


def onde_book(request, book_id: int):
    book = next((book for book in BOOKS if book['id'] == book_id), None)

    if not book:
        return HttpResponseNotFound(f"Book with id={book_id} doesn't exist")

    return render(request, 'bookstore/book.html', context={'book': book})


def onde_author(request, author_id: int):
    author = next((author for author in AUTHORS if author['id'] == author_id), None)

    if not author:
        return HttpResponseNotFound(f"Author with id={author_id} doesn't exist")

    return render(request, 'bookstore/author.html', context={'author': author})
