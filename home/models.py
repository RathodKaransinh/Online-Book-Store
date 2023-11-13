from django.db import models

# Create your models here.
class Order(models.Model):
  label = models.CharField(max_length=20)
  name = models.CharField(max_length=100)
  address = models.CharField(max_length=255)
  uname = models.CharField(max_length=100)
  date = models.DateField
  
  def __str__(self):
    return self.name