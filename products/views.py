from django.shortcuts import render
from django.views import generic
from .models import Product, ProductImages , Brand, Review
# Create your views here.

class ProductList(generic.ListView):
    model=Product

class ProductDetail(generic.DetailView):
    model=Product   
    
     