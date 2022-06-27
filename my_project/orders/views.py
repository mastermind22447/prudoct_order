from multiprocessing import context
from django.template import loader
from django import template
from django.shortcuts import render
from django.http import HttpResponse
from .models import Orders


def orders(request):
    orders = Orders.objects.all()
    context = {
        "orders" : orders,
    }
    template = loader.get_template('base/orders.html')

    print('----')
    print(orders)
    return HttpResponse(template.render(context, request))
   

def add_order():
    return


def completed_orders():
    return