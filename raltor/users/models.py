from __future__ import unicode_literals
from django.db import models


class client(models.Model):
      user_name = models.CharField(max_length=50)
      mobilenumber = models.IntegerField()
      email = models.EmailField()
      address = models.CharField(max_length=50)
      password = models.CharField(max_length=50)
      
      def __str__(self):
       return self.user_name


class clientauth(models.Model):
    authdata = models.ForeignKey(client,on_delete=models.CASCADE)
    name = models.CharField(blank=True,null=True , max_length= 10)
    
    def getuser_name():
        data = list(client.objects.values_list('user_name'))
        return data

    def getPassword():
        password = list(client.objects.values_list('password'))
        return password
    
    def getID():
        password = list(client.objects.values_list('id'))
        return password


class Product(models.Model):
    
       legnth=models.IntegerField()
       width=models.IntegerField()
       house_id=models.IntegerField(max_length=1,null=True,blank=True)
       location=models.CharField(max_length=100)
       price=models.IntegerField()
       size=models.IntegerField()
       product_type=models.CharField(max_length=10)
       num_of_bedrooms=models.IntegerField(max_length=2)
       num_of_bathrooms=models.IntegerField(max_length=2)
       about=models.TextField(max_length=200)    
       image=models.ImageField(upload_to='Product') 
       slug=models.SlugField(null=True,blank=True)
       
       def __str__(self):
          return self.location 
      