from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class Bag(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def total(self):
        return sum(item.subtotal() for item in self.items.all())


class BagItem(models.Model):
    bag = models.ForeignKey(Bag, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def subtotal(self):
        return self.product.price * self.quantity
