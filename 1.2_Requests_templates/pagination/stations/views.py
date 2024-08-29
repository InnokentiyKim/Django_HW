from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
import csv


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    with open(settings.BUS_STATION_CSV, newline='') as csvfile:
        stations_reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
        stations_list = [row for row in stations_reader]
    paginator = Paginator(stations_list, settings.CONTENT_ON_PAGE)
    requested_page = request.GET.get('page', 1)
    page = paginator.get_page(requested_page)
    context = {
        'bus_stations': page.object_list,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
