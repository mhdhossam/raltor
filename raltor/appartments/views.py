from __future__ import unicode_literals
from django.shortcuts import render
from.models import Product



# Create your views here.s
def appartment(request,name):
    Product1=Product.objects.all()
    name='a'
    return render(request,'apprtments-1.html',{'rs':Product1})


def appartmentcity(request,slug):
    

    Product_city=Product.objects.filter(slug=slug)
    
    return render(request,'apprtments-city.html',{'rs2':Product_city})


def details(request,house_id):
    product_info=Product.objects.get(house_id=house_id)

    return render(request,'aprtmebt-information.html', {'rs3':product_info})



