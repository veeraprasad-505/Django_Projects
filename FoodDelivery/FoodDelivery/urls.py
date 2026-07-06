from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('restaurants/', include('Restaurants.urls')),
    path('menu/', include('Menu.urls')),
    path('orders/', include('Orders.urls')),
]
