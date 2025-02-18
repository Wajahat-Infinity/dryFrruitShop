from django.shortcuts import render
from urllib import request
from django.http import HttpResponse
from django.views import View 
from . models import Product
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm, CustomAuthenticationForm

# Create your views here.
def home(request):
    return render(request,"app/home.html")

def about(request):
    return render(request,"app/about.html")

def contact(request):
    return render(request,"app/contact.html")

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

class ProductDetailView(View):
    def get(self,request,pk):
        product=Product.objects.get(pk=pk)
        return render(request,"app/productdetail.html",locals())    
    
# views.py
class CategoryTitleView(View):
    def get(self, request, title):  # Change 'val' to 'title' here
        products = Product.objects.filter(title=title)
        titles = Product.objects.filter(category=products[0].category).values('title')
        context = {
            'title': title,  # Pass 'title' to the context if needed
            'products': products,
            'titles': titles,
        }
        return render(request, "app/category.html", context)

class CustomerRegistrationView(View):
    def get(self,request):
        form=CustomUserCreationForm()
        # context={
        #     'form':form,
        # }
        return render(request,"app/customerregistration.html",locals())
    def post(self,request):
        form = CustomAuthenticationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Congratulation! User registration successsful")
        else:
            messages.warning(request,"invalid Data")
            
        return render(request,"app/customerregistration.html",locals())
