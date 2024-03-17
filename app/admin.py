from django.contrib import admin
from .models import Category,Photo
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ['user','name']

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    fields = ['category','image']