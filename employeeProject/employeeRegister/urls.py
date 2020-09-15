from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.employeeForm, name='employeeForm'),
    path('employeeList', views.employeeList, name='employeeList'),
]
