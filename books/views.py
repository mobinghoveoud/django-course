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

    return redirect("books:list")
