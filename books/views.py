from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View

from books.forms import BookCreateForm
from books.models import Book


# def books_list(request):
#     books = Book.objects.all()
#
#     return render(request, "books/list.html", {"books": books})

class BookListView(View):
    def get(self, request):
        books = Book.objects.all()
        return render(request, "books/list.html", {"books": books})


# def detail(request, book_id):
#     book = Book.objects.get(pk=book_id)
#
#     return render(request, "books/detail.html", {"book": book})

class BookDetailView(View):
    def get(self, request, book_id):
        book = Book.objects.get(pk=book_id)

        return render(request, "books/detail.html", {"book": book})


def delete(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    book.delete()
    messages.success(request, f"Book '{book.title}' deleted successfully.", extra_tags="alert alert-success")

    return redirect("books:list")


# def create_author(request):
#     if request.method == "POST":
#         form = AuthorCreateForm(request.POST)
#         # Validation
#         if form.is_valid():
#             Author.objects.create(name=form.cleaned_data["name"], bio=form.cleaned_data["bio"])
#
#             messages.success(
#                 request,
#                 f"Author '{form.cleaned_data['name']}' created successfully.",
#                 extra_tags="alert alert-success"
#             )
#     else:
#         form = AuthorCreateForm()
#
#     return render(request, "authors/create.html", {"form": form})


# def create_book(request):
#     if request.method == "POST":
#         form = BookCreateForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#
#             messages.success(request, f"Book '{form.cleaned_data['title']}' created successfully.",
#                              extra_tags="alert alert-success")
#     else:
#         form = BookCreateForm()
#
#     return render(request, "books/create.html", {"form": form})

class BookCreateView(View):
    form_class = BookCreateForm
    template_name = "books/create.html"

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            messages.success(request, f"Book '{form.cleaned_data['title']}' created successfully.",
                             extra_tags="alert alert-success")

        return render(request, self.template_name, {"form": form})


# def update_book(request, book_id):
#     book = Book.objects.get(pk=book_id)
#
#     if request.method == "POST":
#         form = BookCreateForm(request.POST, request.FILES, instance=book)
#
#         if form.is_valid():
#             form.save()
#
#             messages.success(request, f"Book '{form.cleaned_data['title']}' updated successfully.",
#                              extra_tags="alert alert-success")
#     else:
#         form = BookCreateForm(instance=book)
#
#     return render(request, "books/update.html", {"form": form})


class BookUpdateView(LoginRequiredMixin, View):
    form_class = BookCreateForm
    template_name = "books/update.html"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.book = None

    def setup(self, request, *args, **kwargs):
        self.book = Book.objects.get(pk=kwargs["book_id"])

        super().setup(request, *args, **kwargs)

    def dispatch(self, request, *args, **kwargs):
        if request.user != self.book.author:
            return HttpResponse("Not Allowed!", status=401)

        super().dispatch(request, *args, **kwargs)

    def get(self, request, book_id):
        form = self.form_class(instance=self.book)

        return render(request, self.template_name, {"form": form})

    def post(self, request, book_id):
        form = self.form_class(request.POST, request.FILES, instance=self.book)

        if form.is_valid():
            form.save()

            messages.success(request, f"Book '{form.cleaned_data['title']}' updated successfully.",
                             extra_tags="alert alert-success")

        return render(request, self.template_name, {"form": form})
