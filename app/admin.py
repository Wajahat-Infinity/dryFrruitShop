from django.contrib import admin

from . models import Product

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display=['id','title','selling_price','discount_price','description','composition','prodapp','category','product_image' ]

# Register your models here.
