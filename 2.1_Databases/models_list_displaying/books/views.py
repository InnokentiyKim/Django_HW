from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from books.models import Book
from main.settings import CONTENT_ON_PAGE


def books_view(request):
    template = 'books/books_list.html'
    books = [book for book in Book.objects.all()]
    context = {'books': books}
    return render(request, template, context)

def index_view(request):
    return redirect('books')

def books_pub_date_view(request, pub_date):
    template = 'books/book.html'
    books_list = [book for book in Book.objects.all().order_by('pub_date')]
    requested_page_num = None
    pages_pub_date_list = []
    for i, book in enumerate(books_list, start=1):
        pages_pub_date_list.append(book.pub_date)
        if book.pub_date == pub_date:
            requested_page_num = i
    if not requested_page_num:
        raise Http404
    paginator = Paginator(books_list, CONTENT_ON_PAGE)
    page = paginator.get_page(requested_page_num)
    context = {'book': books_list[requested_page_num - 1],'page': page, 'pages_list': pages_pub_date_list}
    return render(request, template, context)
