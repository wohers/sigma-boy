from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import View
from django.urls import reverse_lazy
from .models import Product

# Create your views here.


class ProductsListView(ListView):
    model = Product
    template_name = 'products_list.html'
    context_object_name = 'products'


class ProductsCreateView(CreateView):
    model = Product
    fields = '__all__'
    template_name = 'products_form.html'
    success_url = reverse_lazy('index')


class ProductsUpdateView(UpdateView):
    model = Product
    fields = '__all__'
    template_name = 'products_from.html'
    success_url = reverse_lazy('index')


class ProductsDeleteView(DeleteView):
    model = Product
    fields = '__all__'
    template_name = 'products_delete.html'
    success_url = reverse_lazy('index')


class ProductsDetailsView(View):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        return render(request, 'product.html', context={'poduct': product})








