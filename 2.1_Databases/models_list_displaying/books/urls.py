from django.urls import path
from books import views

urlpatterns = [
    path('', views.books_view, name='books'),
    # path('', )
]