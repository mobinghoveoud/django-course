from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from books.forms import AuthorCreateForm, BookCreateForm
from books.models import Author, Book


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


def create_author(request):
    if request.method == "POST":
        form = AuthorCreateForm(request.POST)
        # Validation
        if form.is_valid():
            Author.objects.create(name=form.cleaned_data["name"], bio=form.cleaned_data["bio"])

            messages.success(request, f"Author '{form.cleaned_data['name']}' created successfully.",
                             extra_tags="alert alert-success")
    else:
        form = AuthorCreateForm()

    return render(request, "authors/create.html", {"form": form})


def create_book(request):
    if request.method == "POST":
        form = BookCreateForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, f"Book '{form.cleaned_data['title']}' created successfully.",
                             extra_tags="alert alert-success")
    else:
        form = BookCreateForm()

    return render(request, "books/create.html", {"form": form})
