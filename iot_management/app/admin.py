from django.contrib import admin
from .models import CustomUser, Device

admin.site.register(CustomUser)
admin.site.register(Device)
