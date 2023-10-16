from django.shortcuts import render

from books.models import Book


def books_list(request):
    books = Book.objects.all()

    return render(request, "books/list.html", {"books": books})