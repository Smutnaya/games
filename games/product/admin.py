from django.contrib import admin

from .models import Review, Order, Product

# Register your models here.
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Review)