from django.shortcuts import get_object_or_404, render
from .models import Book


def index(request):
    books = Book.objects.all()
    context = {"books": books}
    return render(request, "book_outlet/index.html", context)


# Create your views here.
def book_details(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    context = {"book": book}
    return render(request, "book_outlet/book_details.html", context)
