from __future__ import unicode_literals 
from django.db import models
from django.utils.text import slugify

# Create your models here.

class Product(models.Model):
       length=models.IntegerField(null=True,blank=True)
       width=models.IntegerField(null=True,blank=True)
       product_name=models.CharField(max_length=50)
       house_id=models.IntegerField(max_length=1,null=True,blank=True)
       location=models.CharField(max_length=100)
       price=models.IntegerField()
       size=models.IntegerField()
       style=models.CharField(max_length=50)
       product_type=models.CharField(max_length=10)
       num_of_bedrooms=models.IntegerField(max_length=2)
       num_of_bathrooms=models.IntegerField(max_length=2)
       about=models.TextField(max_length=200)    
       image=models.ImageField(upload_to='Product') 
       slug=models.SlugField(null=True,blank=True)
       
       def __str__(self):
          return self.location 
      

   
        