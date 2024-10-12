from django.shortcuts import render
from urllib import request
from django.http import HttpResponse
from django.views import View 
from . models import Product

# Create your views here.
def home(request):
    return render(request,"app/home.html")

class CategoryView(View):
    def get(self, request, val):
        # Filter products based on the category value (e.g., 'AP' for APRICOT)
        products = Product.objects.filter(category=val)
        
        # Pass both 'val' and 'products' to the template
        context = {
            'val': val,
            'products': products
        }
        
        # Render the template with the updated context
        return render(request, "app/category.html", context)