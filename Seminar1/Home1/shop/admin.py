from django.contrib import admin

# Register your models here.
from .models import Product, Order, Client

admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Client)
