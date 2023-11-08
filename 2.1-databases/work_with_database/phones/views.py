from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort', 'name')
    if sort == 'name':
        phone_objects = Phone.objects.all().order_by(sort)
    elif sort == 'min_price':
        phone_objects = Phone.objects.all().order_by('price')
    else:
        phone_objects = Phone.objects.all().order_by('-price')
    context = {'phones': phone_objects}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.filter(slug=slug).first()
    context = {'phone': phone}

    return render(request, template, context)
