from django.shortcuts import render
from myapp.models import Contact
# Create your views here.

def hello_world(request):
    return render(request,'index.html')
    

def contact(request):
    if request.method =="POST":
        email=request.POST.get("email")
        password=request.POST.get("password")
        data=Contact(email=email,password=password)
        data.save()
    return render(request,'form.html')
