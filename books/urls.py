from django.urls import path

from books import views

app_name = "books"

urlpatterns = [
    path("", views.books_list, name="list"),
    path("<int:book_id>/", views.detail, name="detail"),
    path("<int:book_id>/delete/", views.delete, name="delete"),

    path("create/", views.create_book, name="create-book"),
    path("author/create/", views.create_author, name="create-author"),

    path("<int:book_id>/update/", views.update_book, name="update-book"),
]
