from django.urls import path, register_converter
from books import views
from . import converters

register_converter(converters.DateConverter, 'pub_date')

urlpatterns = [
    path('', views.books_view, name='books'),
    path('<pub_date:pub_date>', views.books_pub_date_view, name='books_pub_date'),
]