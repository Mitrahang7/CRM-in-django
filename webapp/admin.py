from django.contrib import admin
from .models import Client,Product


class ClientAdmin(admin.ModelAdmin):
  list_display=('full_name','email','created_at')

class ProductAdmin(admin.ModelAdmin):
  list_display=('client','name', 'price')
  

admin.site.register(Client,ClientAdmin)

admin.site.register(Product,ProductAdmin)