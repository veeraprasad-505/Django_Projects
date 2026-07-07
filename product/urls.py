from django.urls import path
from . import views

urlpatterns = [
    path('products/add/', views.add_product, name='add-product'),
    path('products/', views.get_products, name='get-products'),
    path('products/update/<int:id>/', views.update_product, name='update-product'),
    path('products/delete/<int:id>/', views.delete_product, name='delete-product'),
]
