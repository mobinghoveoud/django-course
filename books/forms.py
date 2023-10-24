from django import forms

from books.models import Book


class AuthorCreateForm(forms.Form):
    name = forms.CharField()
    bio = forms.CharField(widget=forms.Textarea)


class BookCreateForm(forms.ModelForm):
    class Meta:
        model = Book
        # fields = ["title", "description", "author", "price", "publication_date", "cover"]
        fields = "__all__"
        widgets = {
            "publication_date": forms.widgets.DateInput(attrs={"type": "date"})
        }
