from django.urls import path

from books.views import books_list, detail, delete, create_author

app_name = "books"

urlpatterns = [
    path("", books_list, name="list"),
    path("<int:book_id>/", detail, name="detail"),
    path("<int:book_id>/delete/", delete, name="delete"),
    path("author/create/", create_author, name="create-author")
]
