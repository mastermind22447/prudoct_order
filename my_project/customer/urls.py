from django.urls import path
from . import views

urlpatterns = [
    path('', views.customers, name='customers'),
    path('customer_detail/<int:customer_id>/', views.customer_detail, name='customer_detail'),
    path('add_customer/', views.add_customer, name='add_customer'),
    path('add_customer/insert/', views.insert_customer, name='insert_customer'),
    path('edit_customer/<int:customer_id>/', views.edit_customer, name='edit_customer'),
    path('update_customer/<int:customer_id>/', views.update_customer, name='update_customer'),
    path('delete_customer/<int:customer_id>/', views.delete_customer, name='delete_customer'),
    path('api_customers/', views.customers, name='api_customers')
]