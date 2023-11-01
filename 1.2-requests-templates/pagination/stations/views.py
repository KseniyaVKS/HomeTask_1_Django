from django.shortcuts import render, redirect
from django.urls import reverse
import csv
from django.core.paginator import Paginator

def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице

    with open('data-398-2018-08-30.csv', 'r', encoding='utf-8') as f:
        f_reader = csv.DictReader(f, delimiter=",")
        bus_stations = []
        for row in f_reader:
            bus_stations.append(row)

    page_number = int(request.GET.get("page", 1))
    paginator = Paginator(bus_stations, 5)
    page = paginator.get_page(page_number)

    context = {
        'bus_stations': page,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
