from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def books_list(request):
    return HttpResponse("Lista książek")


def book_details(request, book_id):
    return HttpResponse("Szczegóły książki")
