from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from django.db.models import Q, F
from django.db.models.functions import Lower


def all_products(request):
    products = Product.objects.all()
    categories = Category.objects.all()

    query = request.GET.get('s', None)
    selected_category = request.GET.get('category', None)
    sort = request.GET.get('sort', None)
    direction = request.GET.get('direction', 'asc')

    # Search
    if query:
        products = products.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query)
        )

    # Category filtering
    if selected_category:
        products = products.filter(category__id=selected_category)

    # Sorting
    if sort:
        sortkey = sort

        if sort == 'name':
            sortkey = 'lower_name'
            products = products.annotate(lower_name=Lower('name'))

        elif sort == 'category':
            sortkey = 'category__name'

        elif sort == 'price':
            sortkey = 'price'

        elif sort == 'rates':
            sortkey = 'rates'

        if direction == 'desc':
            sortkey = f'-{sortkey}'

        products = products.order_by(sortkey)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'categories': categories,
        'search_term': query,
        'current_categories': selected_category,
        'current_sorting': current_sorting,
        'sort': sort,
        'direction': direction,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
