from django.shortcuts import render
from .models import Bag

def view_bag(request):
    bag = getattr(request.user, 'bag', None)
    if not bag:
        bag = Bag.objects.create(user=request.user)

    context = {
        'bag_items': bag.items.all(),
        'grand_total': bag.total(),
    }
    return render(request, 'bag/bag.html', context)

