from multiprocessing import context

from django.template import loader
from django import template
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse



from .models import Orders
from .forms import OrderForm
from customer.forms import CustomerForm
from customer.models import Customer


def orders(request):
    orders = Orders.objects.all()
    context = {
        "orders" : orders,
    }
    template = loader.get_template('base/orders.html')

    # print('-------------------')
    
    # print(orders)
    return HttpResponse(template.render(context, request))


def add_order(request):
    form = OrderForm(request.POST or None)
    if form.is_valid():
        form.save()
    
    context = {
        'form' : form
        
    }
    
    return render(request, 'base/add_order.html', context)

def insert(request):
   customer = request.POST.get('customer')
   customer = Customer()
   customer.save()
   name = request.POST.get('name')
   quantity = request.POST.get('quantity')
   order = Orders()
   order.name = name
   order.quantity = quantity
   order.save()

#    print(customer)
   

   return redirect('orders')


def completed_orders():
    return