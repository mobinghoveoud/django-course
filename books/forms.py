from django import forms
from django.core.exceptions import ValidationError

from books.models import Book


# class AuthorCreateForm(forms.Form):
#     name = forms.CharField()
#     bio = forms.CharField(widget=forms.Textarea)


class BookCreateForm(forms.ModelForm):
    class Meta:
        model = Book
        # fields = ["title", "description", "author", "price", "publication_date", "cover"]
        fields = "__all__"
        widgets = {
            "publication_date": forms.widgets.DateInput(attrs={"type": "date"})
        }

    def clean_price(self):
        if self.cleaned_data["price"] < 50000:
            raise ValidationError("price must be 50000 or bigger.")

        return self.cleaned_data["price"]


class BookCreateWithAuthorForm(forms.ModelForm):
    class Meta:
        model = Book
        exclude = ("author",)
        widgets = {
            "publication_date": forms.widgets.DateInput(attrs={"type": "date"})
        }

    def __init__(self, *args, **kwargs):
        self.author = kwargs.pop("author", None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        obj = super().save(commit=False)
        obj.author = self.author
        obj.save()

        return obj
