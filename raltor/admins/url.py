from django.urls import path,include
from . import views
app_name='admins'
urlpatterns = [
    path('admin',views.admin,name='admin'),
    path('uploadreq',views.uploadreq,name='uploadreq'),
    path('chatadmin',views.chatadmin,name='chatadmin'),
]