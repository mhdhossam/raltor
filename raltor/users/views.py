
from __future__ import unicode_literals
from django.shortcuts import render,redirect
from django.contrib import messages
from .check import checkData
from .models import client,clientauth
from appartments.models import Product
def signup(request):
   
    user_name=request.POST.get('user_name')
    password = request.POST.get('password')
    mobilenumber = request.POST.get('mobilenumber')
    address = request.POST.get('address')
    email=request.POST.get('email')
    data=client(user_name=user_name,
    email=email,
    password=password,
    mobilenumber=mobilenumber,
    address=address
    )


   
  
    
    if request.method=='POST':
     data.save()
    name = 'a'
    return render(request,'login/login.html',{'rs2': name})


def login(request):
    if request.method=='POST':       
     user_name1=request.POST['Username']
     password1=request.POST['Password']
    
     user_name= clientauth.getuser_name()
     password = clientauth.getPassword()
     checked =  checkData(request,user_name,user_name1,password,password1)
     if checked :
         return render(request,'logincheck/loginchecked.html',{'rs':user_name1})
     else:
          messages.error(request,'kindly check your email and password :(')
      #   return render(request,'patientlogin/index.html',{'rs':password,'vs':email[i][0]})
    name = 'a'
    return render(request,'login/login.html',{'rs2': name}) 


def logincheck(request,name):
   pr4 = client.objects.all()
   pr1 = client.objects.get(user_name = name)
   return render(request,'home/home.html',{'rs1':pr1})

def addproduct(request):

    name1=request.POST.get('product_name')
    about = request.POST.get('about')
    location = request.POST.get('location')
    product_type = request.POST.get('product_type')
    style=request.POST.get('style')
    area=request.POST.get('area')
    price = request.POST.get('price')
    length1 = request.POST.get('length')
    width = request.POST.get('width')
    num_of_bedrooms=request.POST.get('num_of_bedrooms')
    num_of_bathrooms = request.POST.get('num_of_bathrooms')
    image=request.FILES.get('image')

    data=Product(product_name=name1,
    about=about,
    location=location,
    product_type=product_type,
    style=style,
    size=area,
    price=price,
    length=length1,
    width=width,
    num_of_bedrooms=num_of_bedrooms,
    num_of_bathrooms=num_of_bathrooms,
    image=image,
    )
    
    
    
    if request.method=='POST':
        data.save()
    name = 'a'
    return render(request,'addproduct/add-product.html',{'rs2':name})


def contactus(request):
   
   return render(request,'contactus/contact-us.html')


def home(request, name):
   pr1 = client.objects.filter(user_name = name)
   pr2 = pr1.filter(user_name = name)
   pr3 = pr2
   
   return render(request,'home/home.html',{'rs2':pr3})

def payment(request):
   
   return render(request,'payment/payment.html')



def comingsoon(request):
   
   return render(request,'comingsoon/coming-soon.html')

def chatuser(request):
   
   return render(request,'chatuser/chat-user.html')

def profileuser(request,name):
   
   name='a'
   return render(request,'userprofile/profile-user.html',{'rs2':name})

def profileusersetting(request, name):
   # pr1 = client.objects.filter(user_name = name1)
   # pr2 = pr1.filter(user_name = name1)
   # pr3 = pr2
   name = 'a'
   return render(request,'userprofilesettings/user-profile-sittings.html',{'rs2':name})