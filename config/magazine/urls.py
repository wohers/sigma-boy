from django.urls import path
from .views import (
    ProductsListView,
    ProductsCreateView,
    ProductsUpdateView,
    ProductsDeleteView,
    ProductsDetailsView,
)

urlpatterns = [
    path('', ProductsListView.as_view(), name='products_list'),
    path('product_detail/<int:pk>/', ProductsDetailsView.as_view(), name='product_detail'),
    path('create/', ProductsCreateView.as_view(), name='product_create'),
    path('update/<int:pk>', ProductsUpdateView.as_view(), name='product_update'),
    path('delete/<int:pk>', ProductsDeleteView.as_view(), name='product_delete'),
]