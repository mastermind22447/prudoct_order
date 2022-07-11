from django.shortcuts import render, redirect
from .models import Customer 
from orders.models import Orders
from django.http import HttpResponse
from django.template import loader
from django.db.models import Sum
from .utils import getCustomers
from rest_framework.decorators import api_view

def customers(request):
    customers = Customer.objects.all
    context = {
        'customers' : customers
    }
    template = loader.get_template('customer_base/customers.html')

    return HttpResponse(template.render(context, request))

def add_customer(request):
    customer = Customer.objects.all()
    context = {
        'customer' : customer
    }

    return render(request, 'customer_base/add_customer.html')

def customer_detail(request, customer_id):
    orders = Orders.objects.filter(customer_id=customer_id)
    order_numb = orders.aggregate(Sum("quantity"))
    template = loader.get_template('customer_base/customer_detail.html')
    context = {
        'orders' : orders,
        'order_numb' : order_numb,
    }

    return HttpResponse(template.render(context, request))

def insert_customer(request):
    name = request.POST.get('customer_name')
    customer = Customer()
    customer.name = name
    customer.save()
    return redirect('customers')

def edit_customer(request, customer_id):
    customer = Customer.objects.get(pk=customer_id)
    context = {
        'customer' : customer
    }
    template = loader.get_template('customer_base/customer_edit.html')
    return HttpResponse(template.render(context, request))

def update_customer(request, customer_id):
    customer = Customer.objects.get(pk=customer_id)
    name = request.POST.get('customer_name')
    customer.name = name
    customer.save()
    return redirect('customers')

def delete_customer(request, customer_id):
    customer = Customer.objects.filter(id=customer_id).delete()
    return redirect('customers')

@api_view(['GET'])
def customers(request):
    return getCustomers(request)