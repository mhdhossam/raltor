
from __future__ import unicode_literals
from django.urls import path,include
from . import views

app_name='users'
urlpatterns = [
    path('home/<str:name>',views.home,name='home'),
    path('login',views.login,name='login'),
    path('logincheck/<str:name>',views.logincheck,name='logincheck'),
    path('signup',views.signup,name='signup'),
    path('addproduct',views.addproduct,name='addproduct'),
    path('contactus',views.contactus,name='contactus'),
    path('payment',views.payment,name='payment'),
    path('comingsoon',views.comingsoon,name='comingsoon'),
    path('chatuser',views.chatuser,name='chatuser'),
    path('profileuser/<str:name>',views.profileuser,name='profileuser'),
    path('profileusersetting',views.profileusersetting,name='profileusersetting'),
] 
