from django.shortcuts import render, HttpResponse
from datetime import datetime 
from home.models import Contact
from django.contrib import messages

def index(request):
    # return HttpResponse("this is home page")
   context ={
        "variable1":"Harikesh is great",
        "variable2":"you are also great"
        }
   messages.success(request, "Profile details updated.")
   return render(request, 'index.html',context)

def about(request):
    # return HttpResponse("this is about page")
       return render(request, 'about.html')

def services(request):
    # return HttpResponse("this is services page")
    return render(request, 'services.html')


def contact(request):
    if request.method == "POST":
         name= request.POST.get('name')
         email=request.POST.get('email')
         phone=request.POST.get('phone')
         desc=request.POST.get('desc')
         contact= Contact(name=name, email=email, phone=phone, desc=desc,date=datetime.today())
         contact.save()
         messages.success(request, "Your data submitted!")
    # return HttpResponse("this is contact page")
    return render(request, 'contact.html')


# Create your views here.
