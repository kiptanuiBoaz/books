from django.contrib import admin

from .models import Book, Country, Address


class BookAdmin(admin.ModelAdmin):
    read_only_fields = ("slug",)
    list_filter = ("rating", "author")


# Register your models here.
admin.site.register(Book, BookAdmin)
admin.site.register(Country)
admin.site.register(Address)  # This line seems redundant and can be removed
