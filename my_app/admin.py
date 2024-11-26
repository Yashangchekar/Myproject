from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Client,Project  # Replace with your model's actual name

admin.site.register(Client)
admin.site.register(Project)
