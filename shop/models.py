from django.db import models

# Create your models here.
from django.db import models
'''
This will be our data structure


+ User - this is a django user created for each custormer that registers with the website.
  This allows the user auth using Djngo Auth


+ Customer - Is a User model to hold one relationship with each user (OneToOneField)


+ Product - Model representing products


+ Order - model will represent a transaction placed or pending


+ OrderItem - one item with an order


+ ShippingAddress - location details
'''
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


# CUSTOMER
class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200)


    def __str__(self):
        return self.name


# PRODUCT
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    digital = models.BooleanField(default=False,null=True, blank=True)


    def __str__(self):
        return self.name
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)


    def __str__(self):
        return str(self.id)


# ORDER ITEM
class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)


# SHIPPING ADDRESS
class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=200, null=False)
    state = models.CharField(max_length=200, null=False)
    zipcode = models.CharField(max_length=200, null=False)
    date_added = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.address


