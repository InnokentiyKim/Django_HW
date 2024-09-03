from django.shortcuts import render
from books.models import Book


def books_view(request):
    template = 'books/books_list.html'
    books_list = [book for book in Book.objects.all()]
    context = {}
    return render(request, template, context)
