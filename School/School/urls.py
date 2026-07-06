from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', include('Students.urls')),
    path('teachers/', include('Teachers.urls')),
    path('classes/', include('Classes.urls')),
]
