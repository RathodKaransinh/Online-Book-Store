from asyncio.windows_events import NULL
import datetime
from urllib import request
from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=50)
 
    @staticmethod
    def get_all_categories():
        return Category.objects.all()
 
    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    selled_by = models.ForeignKey(User, on_delete=models.CASCADE)
    desc = models.TextField(max_length=400)
    price = models.IntegerField()
    stock = models.IntegerField(default=1)
    image = models.FileField(upload_to='static/') 
   
    def __str__(self):
        return self.name
 
    @staticmethod
    def get_product_by_ids(ids):
      return Product.objects.filter(id__in=ids)

    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter(category=category_id)
        else:
            return Product.get_all_products()
    
    @staticmethod
    def get_all_products_by_userid(user_id):
        return Product.objects.filter(selled_by=user_id)
  
class Order(models.Model):
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE)
    customer = models.ForeignKey(User,
                                 on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField(max_length=50, default='', blank=True)
    phone = models.CharField(max_length=50, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.customer) + ' (' + str(self.product.name) + ')'
 
    def placeOrder(self):
        self.save()
 
    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer=customer_id).order_by('-date')