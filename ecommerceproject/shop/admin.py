from django.contrib import admin

# Register your models here.
from .models import Category,Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug':('name',)}


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','price','stock','available','created','updated']
    list_editable = ['price','stock','available']
    prepopulated_fields = {'slug':('name',)}
    list_per_page = 20
    search_fields = ['name']
    list_filter = ['available', 'category']


admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)