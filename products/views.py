from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category
from django.db.models.functions import Lower
from django.db.models import Q
from django.urls import reverse
from django.contrib import messages


def all_products(request):
    products = Product.objects.all()
    categories = Category.objects.all()

    # Search functionality
    query = request.GET.get('s')  # Changed: Search query parameter 's' from the form
    if query:
        products = products.filter(name__icontains=query)  # Changed: Filter products by name matching the query

    # Category filtering functionality (if needed)
    category_filter = request.GET.get('category')  # Changed: Category query parameter
    if category_filter:
        products = products.filter(category__name=category_filter)  # Changed: Filter by category

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
