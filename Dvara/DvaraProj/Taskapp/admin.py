from django.contrib import admin

from .models import Category,SubCategory

# Register your models here.

admin.site.register(Category)
admin.site.register(SubCategory)