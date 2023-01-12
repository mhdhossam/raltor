from django.urls import path,include 

from.import views 


app_name= 'appartments'


urlpatterns= [

 path('appartments',views.appartment,name='appartments'),
 path('appartments/<slug:slug>',views.appartmentcity ,name = 'appartmentcity'),
 path('appartments/info/<int:house_id>',views.details,name='details'),

 

]