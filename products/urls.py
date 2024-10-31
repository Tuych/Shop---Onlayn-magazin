from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.products, name='products'),
    path('products/<int:category_id>', views.products, name='category'),
    path('product/<int:pk>', views.product, name='product'),
    path('products/page/<int:page>', views.products, name='page'),
    path('products/basket-add/<int:product_id>', views.basket_add, name='basket-add'),
    path('products/basket-minus/<int:product_id>', views.basket_minus, name='basket-minus'),
    path('products/basket-delete/<int:product_id>', views.basket_delete, name='basket-delete'),
]
