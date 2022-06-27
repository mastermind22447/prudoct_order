from multiprocessing import context
from unicodedata import name
from django.template import loader
from django import template
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from .models import Orders
from .forms import OrderForm


def orders(request):
    orders = Orders.objects.all()
    context = {
        "orders" : orders,
    }
    template = loader.get_template('base/orders.html')

    print('----')
    
    print(orders)
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
   name = request.POST.get('name')
   quantity = request.POST.get('quantity')
   order = Orders()
   order.name = name
   order.quantity = quantity
   order.save()

   print("---------------------------------------")
   print("name: {name} quantity: {quantity}")

   return redirect('orders')


def completed_orders():
    return