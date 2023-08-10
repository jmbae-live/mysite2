from django.contrib import admin

from shop.models import Product


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'available']
    list_editable = ['name', 'price', 'available']
