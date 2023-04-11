from django.shortcuts import render, redirect
from .models import FoodItem, Order, OrderItem, DeliveryAddress,Category
from django.http import JsonResponse
import json
import datetime
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.views import View

from django.db.models import Q


# Create your views here.


def Home(request):
    return render(request,'customer/home.html')


def Contact(request):
    return render(request, 'customer/contact.html')


def food(request):
    if request.user.is_authenticated:
        # customer = request.user.customer
        order, created = Order.objects.get_or_create(complete=False)
        # order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cart_items = order.get_cart_items
    else:
        # Create empty cart for now for non-logged in user
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'delivery': False}
        cart_items = order['get_cart_items']

    fooditems = FoodItem.objects.all()
    fooditems = None
    categories = Category.get_all_categories()
    categoryID = request.GET.get('category')
    if categoryID:
        fooditems = FoodItem.get_all_fooditems_by_categoryid(categoryID)
    else:
        fooditems = FoodItem.get_all_fooditems()

    data = {}
    data['fooditems'] = fooditems
    data['categories'] = categories
    context = {'fooditems': fooditems, 'cart_items': cart_items, 'categories': categories}
    return render(request, 'customer/food.html', context)


def cart(request):
    if request.user.is_authenticated:
        # customer = request.user.customer
        order, created = Order.objects.get_or_create(complete=False)
        # order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cart_items = order.get_cart_items
    else:
        # Create empty cart for now for non-logged in user
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'delivery': False}
        cart_items = order['get_cart_items']

    context = {'items': items, 'order': order, 'cart_items': cart_items}
    return render(request, 'customer/cart.html', context)


def checkout(request):
    if request.user.is_authenticated:
        # customer = request.user.customer
        order, created = Order.objects.get_or_create(complete=False)
        # order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cart_items = order.get_cart_items
    else:
        # Create empty cart for now for non-logged in user
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'delivery': False}
        cart_items = order['get_cart_items']

    context = {'items': items, 'order': order, 'cart_items': cart_items}
    return render(request, 'customer/checkout.html', context)


def updateItem(request):
    data = json.loads(request.body)
    fooditem_id = data['fooditem_id']
    action = data['action']
    print('Action:', action)
    print('FoodItem:', fooditem_id)

    # customer = request.user.customer
    fooditem = FoodItem.objects.get(id=fooditem_id)
    order, created = Order.objects.get_or_create(complete=False)
    # order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, fooditem=fooditem)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)


def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)
    if request.user.is_authenticated:
        # customer = request.user.customer
        order, created = Order.objects.get_or_create(complete=False)
        # order, created = Order.objects.get_or_create(customer=customer, complete=False)
        total = float(data['form']['total'])
        order.transaction_id = transaction_id

        if total == order.get_cart_total:
            order.complete = True
        order.save()

        if order.delivery == True:
            DeliveryAddress.objects.create(
                # customer=customer,
                order=order,
                address=data['delivery']['address'],
                city=data['delivery']['city'],
                state=data['delivery']['state'],
                zipcode=data['delivery']['zipcode'],
            )
    else:
        print('User is not logged in..')


    return JsonResponse('Payment submitted...!', safe=False)


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        myuser = User.objects.create_user(username, email, pass1)

        myuser.save()

        return redirect('login')

    return render(request, 'customer/register.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            fname = user.username
            return render(request, 'customer/home.html', {'fname': fname})

        else:
            return redirect('home')

    return render(request, 'customer/login.html')

def signout(request):
    logout(request)
    messages.success(request, 'Logged out Successfully!')
    return redirect('home')


class MenuSearch(View):
    def get(self, request, *args,  **kwargs):
        query = self.request.GET.get("q")

        fooditems = FoodItem.objects.filter(
            Q(name__icontains=query) |
            Q(price__icontains=query)
        )

        context = {
            'fooditems': fooditems
        }
        return render(request, 'customer/food.html', context)


class FoodDetails(View):
    def get(self, request, pk):
        fooditem = FoodItem.objects.get(pk=pk)
        return render(request, 'customer/view.html', locals())


class OrderConfirmation(View):
    def get(self, request):
        order = Order.objects.all()

        context = {

        }
        return render(request,'customer/order_confirmation.html',context)
