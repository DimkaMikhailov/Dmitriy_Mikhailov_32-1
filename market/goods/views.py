from django.shortcuts import render
from goods.models import ProductCard, CatalogGroup
from django.http import response

# Create your views here.


def index(request):
    if request.method == 'GET': return render(request, 'products/index.html')


def products(request):
    if request.method == 'GET':

        goods = ProductCard.objects.all()
        data = {'goods': goods}

        return render(request, 'products/products.html', context=data)


def categories(request):
    if request.method == 'GET':

        category = CatalogGroup.objects.all()
        data = {'categories': category}

        return render(request, 'products/categories.html', context=data)


def product_card(request, product_id: ProductCard.id) -> response:
    if request.method == 'GET':

        product = ProductCard.objects.get(id=product_id)
        data = {'product': product}

        return render(request, 'products/product_detail.html', context=data)


def category_card(request, category_id: CatalogGroup.id) -> response:
    if request.method == 'GET':

        category = CatalogGroup.objects.get(id=category_id)
        data = {'category': category}

        return render(request, 'products/category_detail.html', context=data)
