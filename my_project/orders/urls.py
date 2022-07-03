from django.urls import path
from . import views

urlpatterns = [
    path('', views.orders, name='orders'),
    path('order_detail/<int:order_id>/', views.order_detail, name='order_detail'),
    path('edit_order/<int:order_id>/', views.edit_order, name='edit_order'),
    path('update_order/<int:order_id>/', views.update_order, name='update_order'),
    path('delete_order/<int:order_id>/', views.delete_order, name='delete_order'),
    path('customer_detail/<int:customer_id>/', views.customer_detail, name='customer_detail'),
    path('add_order/', views.add_order, name='add_order'),
    path('add_order/insert/', views.insert_order, name='insert'),
    # path('completed_orders/', views.completed_orders, name='completed_orders'),
]