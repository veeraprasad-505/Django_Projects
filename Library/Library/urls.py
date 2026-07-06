from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', include('Books.urls')),
    path('members/', include('Members.urls')),
]
