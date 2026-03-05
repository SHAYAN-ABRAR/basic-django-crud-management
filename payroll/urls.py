from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.payroll_home, name='payroll_home'),
    path('add/', views.add_salary, name='add_salary'),
    path('edit/<int:pk>/', views.edit_salary, name='edit_salary'),
]