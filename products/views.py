from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category


def all_products(request):
    products = Product.objects.all()
    categories = Category.objects.all()

    query = request.GET.get('s')
    if query:
        products = products.filter(name__icontains=query)

    category_filter = request.GET.get('category')
    if category_filter:
        products = products.filter(category__name=category_filter)

    context = {
        'products': products,
        'categories': categories,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
