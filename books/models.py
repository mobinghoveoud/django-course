from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField()

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField()
    publication_date = models.DateField()

    def __str__(self):
        return self.title
