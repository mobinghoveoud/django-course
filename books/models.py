from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    publication_date = models.DateField()

    def __str__(self):
        return self.title