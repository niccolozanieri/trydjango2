from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length= 100)
    description = models.TextField(max_length= 150, blank= True)
    price = models.DecimalField(max_digits= 15, decimal_places= 2)
    summary = models.TextField(max_length= 100, blank= True)
    featured = models.BooleanField(default= False)
