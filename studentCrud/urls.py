"""
URL configuration for studentCrud project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from students.views import *
from students.views import StudentViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'students', StudentViewset, basename='students')

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',home,name='home'),
    # path('add/',add_student,name='addStudent'),
    # path("students/", include("students.urls")),
    # path('delete/<str:slug>/',delete_students,name='deleteStudent'),
    # path('update/<str:slug>/',update_students,name='updateStudent'),
    path('api-auth/', include('rest_framework.urls')),
    path("", include(router.urls))
]
