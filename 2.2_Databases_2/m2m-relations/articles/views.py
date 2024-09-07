from django.shortcuts import render

from articles.models import Article


def articles_list(request):
    template = 'articles/news.html'
    context = {}
    ordering = '-published_at'

    return render(request, template, context)
