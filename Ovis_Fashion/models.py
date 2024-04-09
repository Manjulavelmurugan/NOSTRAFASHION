from django.db import models
from django.contrib.auth.models import User
import datetime
import os

def getFilename(request,Filename):
    my_datetime=datetime.datetime.now().strftime("%Y-%m-%d%H:%M:%S")
    new_filename="%s%s"%(my_datetime,Filename)
    return os.path.join('uploads/',new_filename)

class Category(models.Model):
    name=models.CharField(max_length=150,null=False,blank=False)
    image=models.ImageField(upload_to=getFilename,null=True,blank=True)
    description=models.TextField(max_length=500,null=False,blank=False)
    status=models.BooleanField(default=True,help_text="0-show,1-Hidden")
    created_at=models.DateTimeField(auto_now_add=True)


    def __str__(self) :
        return self.name
    
class Products(models.Model):
    Category=models.ForeignKey(Category,on_delete=models.CASCADE)
    name=models.CharField(max_length=150,null=False,blank=False)
    vendor=models.CharField(max_length=150,null=False,blank=False)
    product_image=models.ImageField(upload_to='product_images/',null=True,blank=True)
    quantity=models.IntegerField(null=False,blank=False)
    original_price=models.IntegerField(null=False,blank=False)
    selling_price=models.IntegerField(null=False,blank=False)
    description=models.TextField(max_length=500,null=False,blank=False)
    status=models.BooleanField(default=False,help_text="0-show,1-Hidden")
    trending=models.BooleanField(default=False,help_text="1-default,1-trending")
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return self.name
        

