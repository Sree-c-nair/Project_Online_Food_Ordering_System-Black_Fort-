from django.contrib import admin
from .models import Category
from .models import FoodItem
from .models import Order
from .models import Customers
from .models import DeliveryAddress
from .models import OrderItem
# Register your models here.


class AdminFood(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Category)
admin.site.register(FoodItem, AdminFood )
admin.site.register(Order)
admin.site.register(Customers)
admin.site.register(DeliveryAddress)
admin.site.register(OrderItem)

