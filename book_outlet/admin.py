from django.contrib import admin

from .models import Book


class BookAdmin(admin.ModelAdmin):
    read_only_fields = ("slug",)
    list_filter = ("rating", "author")


# Register your models here.
admin.site.register(Book, BookAdmin)
