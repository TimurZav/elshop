from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from django.core.serializers import serialize


def index(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'catalog/index.html', context)


def detail_products(request, category):
    product_list = Product.objects.filter(category__slug=category)
    context = {'products': product_list}
    return render(request, 'catalog/products.html', context)


def filter_view(request):
    category = request.GET['category']
    if request.GET['direction'] == 'up':
        product_list = Product.objects.filter(category__slug=category).order_by('name')
    else:
        product_list = Product.objects.filter(category__slug=category).order_by('-name')
    return HttpResponse(serialize('json', product_list))