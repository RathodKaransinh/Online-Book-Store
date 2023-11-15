from django.db import models

# Create your models here.
class Order(models.Model):
  label = models.CharField(max_length=20)
  name = models.CharField(max_length=100)
  address = models.CharField(max_length=255)
  uname = models.CharField(max_length=100)
  date = models.DateField(auto_now=True)
  
  def __str__(self):
    return self.name
  
class Product(models.Model):
  name = models.CharField(max_length=100)
  uname = models.CharField(max_length=100)
  desc = models.TextField(max_length=400)
  price = models.IntegerField(blank=True)
  image = models.CharField(max_length=255) 
    
  def __str__(self):
    return self.name