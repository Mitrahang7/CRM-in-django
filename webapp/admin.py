from django.contrib import admin
from .models import Client


class ClientAdmin(admin.ModelAdmin):
  list_display=('full_name','email','created_at')
  

admin.site.register(Client,ClientAdmin)
