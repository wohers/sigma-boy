from django.urls import path
from .views import (
    ProductsListView,
    ProductsCreateView,
    ProductsUpdateView,
    ProductsDeleteView,
    ProductsDetailsView,
)

urlpatterns = [
    # Список товаров
    path('goods/', ProductsListView.as_view(), name='products_list'),

    # Детали товара
    path('goods/<int:pk>/', ProductsDetailsView.as_view(), name='product_detail'),

    # Создание товара
    path('goods/create/', ProductsCreateView.as_view(), name='product_create'),

    # Редактирование товара
    path('goods/<int:pk>/update/', ProductsUpdateView.as_view(), name='product_update'),

    # Удаление товара
    path('goods/<int:pk>/delete/', ProductsDeleteView.as_view(), name='product_delete'),
]