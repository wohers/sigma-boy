from django.urls import path
from .views import (
    ProductsListView,
    ProductsCreateView,
    ProductsUpdateView,
    ProductsDeleteView,
    ProductsDetailsView,
)

urlpatterns = [
    path('goods/', ProductsListView.as_view(), name='products_list'),
    path('goods/<int:pk>/', ProductsDetailsView.as_view(), name='product_detail'),
    path('goods/create/', ProductsCreateView.as_view(), name='product_create'),
    path('goods/<int:pk>/update/', ProductsUpdateView.as_view(), name='product_update'),
    path('goods/<int:pk>/delete/', ProductsDeleteView.as_view(), name='product_delete'),
]