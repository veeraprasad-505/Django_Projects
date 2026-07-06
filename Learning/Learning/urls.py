from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('courses/', include('Courses.urls')),
    path('students/', include('Students.urls')),
    path('trainers/', include('Trainers.urls')),
]
