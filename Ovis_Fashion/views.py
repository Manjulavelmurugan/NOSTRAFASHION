
from django.shortcuts import redirect, render
from Ovis_Fashion.form import CustomUserForm
from . models import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

def home(request):
    products=Products.objects.filter(trending=1)
    return render(request,"Ovis_Fashion/index.html",{"products":products})

def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"logged out Successfully")
    return redirect("/")   

def login_page(request):
    if request.user.is_authenticated:
        return redirect("/") 
    else:
        if request.method=='POST':
            name=request.POST.get('username')
            pwd=request.POST.get('userpassword')
            user=authenticate(request,username=name,userpassword=pwd)
            if user is not None:
                login(request,user)
                messages.success(request,"Logged in Successfully")
                return redirect("/")
            else:
                messages.error(request,"Invalid UserName or Password")
                return redirect("/login")
        return render(request,"Ovis_Fashion/login.html")

def register(request):
    form=CustomUserForm()
    if request.method=='POST':
        form=CustomUserForm (request. POST)
        if form.is_valid ():
          form.save()
          messages.success (request,"Registration Success You can Login Now..!") 
          return redirect('/login')
    return render(request,"Ovis_Fashion/register.html",{'form':form})

def collections(request):
    category=Category.objects.filter()
    return render(request,"Ovis_Fashion/collections.html",{"category":category})

def collectionsview(request,name,):
    if(Category.objects.filter(name=name)):
        products=Products.objects.filter(Category__name=name)
        return render(request,"Ovis_Fashion/products/index.html",{"products":products,"category_name":name})
    else:
        messages.warning(request,"No such Category Found")
        return redirect('collections')
    
def product_detials(request,cname,pname):
    if (Category.objects.filter(name=cname)):
        if(Products.objects.filter(name=pname)):
            products=Products.objects.filter (name=pname).first()
            return render(request,"Ovis_Fashion/products/product_detials.html",{"products":products})
        else:
            messages.error(request,"No such Product Found")
            return redirect('collections')
    else:
         messages.warning(request,"No such Category Found")
         return redirect('collections')    


