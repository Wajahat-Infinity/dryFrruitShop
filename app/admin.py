from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'selling_price', 'discount_price', 'description', 'composition', 'prodapp', 'category', 'product_image']
    # list_filter = ['category', 'prodapp']  # Add filters based on category and product application
    # search_fields = ['title', 'description']  # Enable search by title and description
    # ordering = ['id']  # Sort by ID in the list view

# Register your models here. 
