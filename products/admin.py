from django.contrib import admin
from .models import Category, Product


admin.site.register(Category)


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'tool_type',
        'moon_phase',
        'price',
        'rates',
    )


admin.site.register(Product, ProductAdmin)
