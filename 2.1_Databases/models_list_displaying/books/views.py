from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from books.models import Book
from datetime import date


def books_view(request):
    template = 'books/books_list.html'
    books = [book for book in Book.objects.all()]
    context = {'books': books}
    return render(request, template, context)

def index_view(request):
    return redirect('books')


class PageSlugByDate:
    def __init__(self, books_pub_date_seq: list[date], book_pub_date: date):
        self.size = len(books_pub_date_seq)
        self.books_pub_date_seq = books_pub_date_seq
        self.book_pub_date = book_pub_date
        self.current_ind = books_pub_date_seq.index(book_pub_date)

    def has_previous(self):
        return self.current_ind > 0

    def has_next(self):
        return self.current_ind < self.size - 1

    def get_previous_page_slug(self):
        if self.has_previous():
            return self.books_pub_date_seq[self.current_ind - 1]
        else:
            return self.book_pub_date

    def get_next_page_slug(self):
        if self.has_next():
            return self.books_pub_date_seq[self.current_ind + 1]
        else:
            return self.book_pub_date

    def sort_by_date(self, reverse: bool = False):
        self.books_pub_date_seq.sort(reverse=reverse)
        self.current_ind = self.books_pub_date_seq.index(self.book_pub_date)


def books_pub_date_view(request, pub_date):
    template = 'books/book.html'
    book = get_object_or_404(Book, pub_date=pub_date)
    books_list = [book for book in Book.objects.all().order_by('pub_date')]
    books_pub_date_seq = [book.pub_date for book in books_list]
    pages_by_date = PageSlugByDate(books_pub_date_seq, book.pub_date)
    context = {'book': book, 'pages_by_date': pages_by_date}
    return render(request, template, context)
