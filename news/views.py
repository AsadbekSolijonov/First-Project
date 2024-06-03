from django.http import HttpResponse
from news.models import Product
from django.shortcuts import render


def index(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'news/index.html', context)


def detail(request, pk):
    product = Product.objects.get(pk=pk)
    context = {'product': product}
    return render(request, 'news/detail.html', context)
