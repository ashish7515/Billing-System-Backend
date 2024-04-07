from django.contrib import admin

# Register your models here.

from .models import Product, Customer, UserData, Bill

admin.site.register(UserData)
admin.site.register(Bill)
admin.site.register(Product)
admin.site.register(Customer)

