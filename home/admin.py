from django.contrib import admin
from home.models import Order, Wishlist, Complaint


# Register your models here.
admin.site.register(Order)
admin.site.register(Wishlist)
admin.site.register(Complaint)
