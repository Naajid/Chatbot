from django.db import models

# Create your models here.

class Order(models.Model):
    id_no = models.CharField(max_length=15, default="123ABC")
    item = models.CharField(max_length=50, default="Dell i5 Laptop")
    price = models.IntegerField(default=0)
    def __str__(self):
        return self.item
    
    
class Complaint(models.Model) :
    number = models.IntegerField(default=12)
    desc = models.TextField(default="Not Applicable") 
    status = models.CharField(max_length=10, default="NA")
    reply = models.TextField(max_length=100,default="NA")
    def __str__(self):
        return self.desc

class Wishlist(models.Model):
    item = models.CharField(max_length=30, default="Apple iPhone 12")  
    price = models.IntegerField(default=0)



