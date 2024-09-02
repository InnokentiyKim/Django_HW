from django.shortcuts import render, redirect, get_object_or_404
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort')
    phones = [phone for phone in Phone.objects.all()]
    if sort == 'name':
        phones = sorted(phones, key=lambda phone: phone.name)
    elif sort == 'min_price':
        phones = sorted(phones, key=lambda phone: phone.price)
    elif sort == 'max_price':
        phones = sorted(phones, key=lambda phone: phone.price, reverse=True)
    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = get_object_or_404(Phone, slug=slug)
    context = {'phone': phone}
    return render(request, template, context)
