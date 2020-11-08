from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import plasmaregister
from django.contrib import messages
import json
from django.http import JsonResponse
from datetime import date, timedelta


    
def index(request):
    
    
    return render(request,'home.html')


def register(request):
    if request.method=="POST":
       first_name=request.POST.get('first_name')
       mob_number=request.POST.get('mob_number')
       email_id=request.POST.get('email_id')
       blood_group=request.POST.get('blood_group')
       recovered_date=request.POST.get('recovered_date') 

       pform = plasmaregister(first_name=first_name,mob_number=mob_number,email_id=email_id,
       blood_group=blood_group,recovered_date=recovered_date)
       
       pform.save()
       messages.success(request, 'You Have Successfully Registered')
       
       
       
   
      
    return render(request,'register.html')


def requestt(request):
    
    bloodgroup=request.POST.get('bloodgroup')
    date_cover=date.today()-timedelta(days=27)
    bloodgroup= plasmaregister.objects.filter(blood_group=bloodgroup)
    q = bloodgroup.filter(recovered_date__lt=date_cover).values()

    
    d={}

    for i in q:
        d[i['first_name']]=i['mob_number']
    

    return render(request,'requestt.html',{"d":d})

