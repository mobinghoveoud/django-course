from django.urls import path

from books import views

app_name = "books"

urlpatterns = [
    path("", views.BookListView.as_view(), name="list"),
    path("<int:book_id>/", views.BookDetailView.as_view(), name="detail"),
    path("<int:book_id>/delete/", views.delete, name="delete"),

    path("create/", views.BookCreateView.as_view(), name="create-book"),
    # path("author/create/", views.create_author, name="create-author"),

    path("<int:book_id>/update/", views.BookUpdateView.as_view(), name="update-book"),
]
