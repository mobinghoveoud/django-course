from uuid import uuid4

from django.conf import settings
from django.db import models


# class Author(models.Model):
#     name = models.CharField(max_length=200)
#     bio = models.TextField()
#
#     def __str__(self):
#         return self.name


def book_path(instance, filename):
    name = uuid4().hex
    ext = filename.split(".")[-1]

    return f"books/{instance.author.id}/{name}.{ext}"


class BookManager(models.Manager):
    def get_valuable_books(self):
        return self.filter(price__gte=100000)


class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name="Name")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=9, decimal_places=0)
    description = models.TextField()
    publication_date = models.DateField()
    cover = models.ImageField(upload_to=book_path)

    objects = BookManager()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.pk:
            book = Book.objects.get(pk=self.pk)

            if self.cover != book.cover:
                book.cover.delete(save=False)

        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)

        self.cover.delete(save=False)


# Book.objects.get_valuable_books()
