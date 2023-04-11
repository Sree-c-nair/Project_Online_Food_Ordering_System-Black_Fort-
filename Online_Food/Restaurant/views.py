from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.utils.timezone import datetime
from Customer.models import Order, OrderItem
import json


# Create your views here.
class Dashboard(View):
    def get(self,request,*args,**kwargs):
        order, created = Order.objects.get_or_create(complete=False)
        #get the current date
        today = datetime.today()
        orders = Order.objects.filter(date_ordered__year=today.year, date_ordered__month=today.month, date_ordered__day=today.day)
        #loop throught the orders and add the place value
        total = 0

        if total == order.get_cart_total:
            order.complete = True
        order.save()
        total_revenue = 0

        for order in orders:
            total_revenue += order.get_cart_total
        #pass total number of orders and total revenue into template
        context={
            'orders': orders,
            'total_revenue':total_revenue,
            'total_orders':len(orders)
        }
        return render(request,'restaurant/dashboard.html',context)


