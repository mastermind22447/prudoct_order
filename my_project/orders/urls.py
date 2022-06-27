from django.urls import path
from . import views

urlpatterns = [
    path('', views.orders, name='orders'),
    path('add_order/', views.add_order, name='add_order'),
    path('add_order/insert/', views.insert, name='insert'),
    path('completed_orders/', views.completed_orders, name='completed_orders'),
]