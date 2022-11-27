from dataclasses import dataclass
from .models import Book
from django.http import HttpResponse
from django.shortcuts import render





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
    book =
    print(book)
    return render(
        request,
        'book_details.html',
        {
            "book": book
        }
    )
