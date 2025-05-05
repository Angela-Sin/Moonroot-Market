from django.db import models

class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.friendly_name if self.friendly_name else self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254, null=True, blank=True)
    description = models.TextField()

    # General metadata
    weight = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

    # Magical metadata
    magical_properties = models.TextField(null=True, blank=True)
    moon_phase = models.CharField(max_length=100, null=True, blank=True)
    ingredients = models.TextField(null=True, blank=True)
    tool_type = models.CharField(max_length=100, null=True, blank=True)

    # Visuals
    image = models.ImageField(null=True, blank=True)

    # Pricing
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    rates = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

    def clean(self):
        if self.price is not None and self.price <= 0:
            raise ValidationError('Price must be greater than zero.')

        if self.rates is not None and self.rates <= 0:
            raise ValidationError('Rates must be greater than zero.')
        
    def __str__(self):
        return self.name
