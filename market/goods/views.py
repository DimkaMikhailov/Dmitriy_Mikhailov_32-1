from django.db.models import Q
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from goods.models import ProductCard, CatalogGroup, ProductReviews
from django.http import response
from market.forms import AddProductReviewForm, AddProductForm


def index(request):
    if request.method == 'GET': return render(request, 'products/index.html')


def products(request):
    if request.method == 'GET':
        goods = ProductCard.objects.all()

        if search := request.GET.get('search'):
            # goods = goods.filter(title__icontains=search)
            # goods = goods.filter(title__endswith=search)
            # goods = goods.filter(title__startswith=search)
            goods = goods.filter(Q(title__icontains=search) | Q(description__icontains=search))

        p = Paginator(goods, 3)
        data = {'goods': goods, 'page_range': p.page_range}

        if page := request.GET.get('page'):
            goods = p.page(page).object_list
            data['goods'] = goods
        else:
            data['goods'] = p.page(1).object_list

        return render(request, 'products/products.html', context=data)


def categories(request):
    if request.method == 'GET':
        _categories = CatalogGroup.objects.all()

        if category := request.GET.get('category'):
            _categories = _categories.filter(name__icontains=category)

        data = {'categories': _categories}

        return render(request, 'products/categories.html', context=data)


def product_card(request, product_id: ProductCard) -> response:
    if request.method == 'GET':
        product = ProductCard.objects.get(id=product_id)

        reviews = ProductReviews.objects.filter(product_id=product.id)
        if reviews:
            rating = round(sum([float(r.rating) for r in reviews]) / len(reviews), 1)
        else:
            rating = 0

        form = AddProductReviewForm()

        data = {'product': product,
                'rating': rating,
                'form': form,
                'reviews': reviews,
                'display': 'display: block;'}

        return render(request, 'products/product_detail.html', context=data)

    if request.method == 'POST':
        form_data = request.POST
        form = AddProductReviewForm(form_data)

        product = ProductCard.objects.get(id=product_id)
        data = {'product': product}

        if form.is_valid():
            new_review = ProductReviews(
                review=form.cleaned_data.get('description'),
                rating=form.cleaned_data.get('rating'),
                product_id=product)
            new_review.save()

            data['message'] = 'Review create successfully.'
            data['display'] = 'display: none;'
            data['rating'] = 0

            reviews = ProductReviews.objects.filter(product_id=product.id)
            if reviews:
                data['rating'] = round(sum([float(r.rating) for r in reviews]) / len(reviews), 1)
                data['reviews'] = reviews
        else:
            data['form'] = form
        return render(request, 'products/product_detail.html', context=data)


def category_card(request, category_id: CatalogGroup.id):
    if request.method == 'GET':

        category = CatalogGroup.objects.get(id=category_id)
        data = {'category': category}

        return render(request, 'products/category_detail.html', context=data)


def add_product(request):
    user = request.user
    if user.is_authenticated:
        print(user.pk)
        if request.method == 'GET':
            data = {'form': AddProductForm}
            return render(request, 'products/add_product.html', context=data)

        if request.method == 'POST':
            data, files = request.POST, request.FILES
            form = AddProductForm(data, files)
            if form.is_valid():
                product = ProductCard(image=form.cleaned_data.get('image'),
                                      title=form.cleaned_data.get('title'),
                                      description=form.cleaned_data.get('description'),
                                      price=form.cleaned_data.get('price'),
                                      count=form.cleaned_data.get('count'),
                                      in_stock=True if int(form.cleaned_data.get('count')) > 0 else False,
                                      author=user)
                product.save()

                catalog_groups = CatalogGroup.objects.filter(id__in=form.cleaned_data.get('categories'))
                product.catalog_group.add(*catalog_groups)

                return redirect(to=product_card, product_id=product.id)

            return render(request, 'products/add_product.html', context={'form': form})
    else:
        return redirect(to='/users/login/')
