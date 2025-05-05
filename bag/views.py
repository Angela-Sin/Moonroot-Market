from django.shortcuts import render, redirect, get_object_or_404
from .models import Bag
from products.models import Product


def view_bag(request):
    """A view to allow the user to see the contents of their bag"""
    
    bag = request.session.get('bag', {})
    
    bag_items = []
    total = 0
    product_count = 0

    for item_id, quantity in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        item_total = product.price * quantity
        total += item_total
        product_count += quantity
        
        bag_items.append({
            'item_id': item_id,
            'product': product,
            'quantity': quantity,
            'item_total': item_total,
        })

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
    }

    return render(request, 'bag/bag.html', context)


def add_to_bag(request, item_id):
    """Add a specified quantity of an item to the bag in the session"""
    
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    
    bag = request.session.get('bag', {})

    if item_id in bag:
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag
    
    return redirect(redirect_url)