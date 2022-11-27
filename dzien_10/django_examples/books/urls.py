from django.urls import path
from .views import books_list, book_details

# odpowiada za wszystko co jest po /books/ w ścieżce
urlpatterns = [
    path("", books_list),
    path("<int:book_id>", book_details),
]
