from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from .models import Product

# Create your views here.


def index(request):
    return HttpResponse('dffdsfgdf')


class ProductsListView(ListView):
    model = Product
    template_name = 'products_list.html'
    context_object_name = 'products'





