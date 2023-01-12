from __future__ import unicode_literals
from django.shortcuts import render

def admin(request):
   
   return render(request,'adminpage/admin-page.html')

def uploadreq(request):
   
   return render(request,'uploadrequest/reguest-uplaod.html')

def chatadmin(request):
   
   return render(request,'chatadmin/chat-admin.html')