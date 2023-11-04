from django.contrib import admin

from books.models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ["title", "price", "author",
                    # "author.is_superuser"
                    ]
    list_filter = ["author", "publication_date"]
    list_per_page = 1

    fieldsets = (
        (None, {"fields": ["title", "author", "price", "description", ]}),
        ("Other fields", {"fields": ["publication_date", "cover"]})
    )

# admin.site.register(Book, BookAdmin)
