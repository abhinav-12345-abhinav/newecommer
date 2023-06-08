from django.contrib import admin

# Register your models here.
from .models import Category,Product
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug','image']
    prepopulated_fields={ 'slug':('name',)}
admin.site.register(Category,CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','price','stock','available','created','updated','image']
    list_editable = ['price','stock','available','image']
    prepopulated_fields={'slug':('name',)}
    list_per_page = 20
admin.site.register(Product,ProductAdmin)
