from django.shortcuts import render, get_object_or_404, redirect
from books.models import Book


def books_view(request):
    template = 'books/books_list.html'
    books = [book for book in Book.objects.all()]
    context = {'books': books}
    return render(request, template, context)

def index_view(request):
    return redirect('books')

def books_pub_date_view(request, pub_date):
    template = 'books/book.html'
    book_by_date = get_object_or_404(Book, pub_date=pub_date)
    context = {'book': book_by_date}
    return render(request, template, context)
