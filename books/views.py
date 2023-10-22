from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from books.models import Book


def books_list(request):
    books = Book.objects.all()

    return render(request, "books/list.html", {"books": books})


def detail(request, book_id):
    book = Book.objects.get(pk=book_id)

    return render(request, "books/detail.html", {"book": book})


def delete(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    book.delete()
    messages.success(request, f"Book '{book.title}' deleted successfully.", extra_tags="alert alert-success")

    return redirect("books:list")
