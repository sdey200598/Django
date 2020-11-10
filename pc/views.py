from django.shortcuts import render, HttpResponse
from datetime import datetime
from pc.models import Contact
from django.contrib import messages
# Create your views here.
def index(request):
    context={
        'variable1':'this is sent',
        'variable2':'swarup is sent'    
    }
    return render(request,'123.html',context)
    # return HttpResponse("This is Home page")
def about(request):
    return render(request,'about.html')
    # return HttpResponse("This is About page")
def contacts(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact=Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request,"Your information has been sent!")
    return render(request,'contacts.html')
    # return HttpResponse("This is Contact page")