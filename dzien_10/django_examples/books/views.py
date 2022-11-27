from dataclasses import dataclass
from .models import Book
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404


# Create your views here.

def books_list(request):
    books = Book.objects.all()
    return render(
        request,
        'books.html',
        {
            "books": books
        }
    )


def book_details(request, book_id):
    # book = Book.objects.get(id=book_id)
    book = get_object_or_404(Book, id=book_id)
    return render(
        request,
        'book_details.html',
        {
            "book": book
        }
    )
