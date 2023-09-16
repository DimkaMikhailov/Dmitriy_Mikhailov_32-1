from django.shortcuts import render
from goods.models import ProductCard

# Create your views here.


def index(request):
    if request.method == 'GET': return render(request, 'products/index.html')


def products(request):
    if request.method == 'GET':

        goods = ProductCard.objects.all()
        data = {'goods': goods}

        return render(request, 'products/products.html', context=data)
