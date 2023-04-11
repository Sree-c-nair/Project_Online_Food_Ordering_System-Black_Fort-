from django.db import models
from django.contrib.auth.models import User


# from .category import Category

# Create your models here.


class Customers(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, related_name="customer" )
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)

    @staticmethod
    def get_all_categories():
        return Category.objects.all()

    def __str__(self):
        return self.name


class FoodItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=7,decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=200, default='', blank=True, null=True)
    digital = models.BooleanField(default=False, null=True, blank=True)
    image = models.ImageField(upload_to='media/', null=True, blank=True)

    @staticmethod
    def get_fooditems_by_id(ids):
        return FoodItem.objects.filter(id__in=ids)

    @staticmethod
    def get_all_fooditems():
        return FoodItem.objects.all()

    @staticmethod
    def get_all_fooditems_by_categoryid(category_id):
        if category_id:
            return FoodItem.objects.filter(category=category_id)
        else:
            return FoodItem.get_all_fooditems()

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class Order(models.Model):
    customer = models.ForeignKey(Customers, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=True)
    transaction_id = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.id)

    @staticmethod
    def get_all_orders():
        return Order.objects.all()

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total

    @property
    def delivery(self):
        delivery = False
        orderitems = self.orderitem_set.all()
        for i in orderitems:
            if i.fooditem.digital == False:
                delivery = True
        return delivery


class OrderItem(models.Model):
    fooditem = models.ForeignKey(FoodItem, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.fooditem.price * self.quantity
        return total


class DeliveryAddress(models.Model):
    customer = models.ForeignKey(Customers, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=200, null=False)
    state = models.CharField(max_length=200, null=False)
    zipcode = models.CharField(max_length=200, null=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
