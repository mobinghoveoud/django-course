from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver

from books.models import Book


@receiver(post_delete, sender=Book)
def auto_delete_book_cover_on_delete(sender, instance, **kwargs):
    instance.cover.delete(save=False)


@receiver(pre_save, sender=Book)
def auto_delete_book_cover_pre_save(sender, instance, **kwargs):
    if not instance.pk:
        return

    book = Book.objects.get(pk=instance.id)

    if instance.cover != book.cover:
        book.cover.delete(save=False)
