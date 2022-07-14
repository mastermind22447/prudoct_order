from django.template import loader
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Orders
from customer.models import Customer
from pprint import pp, pprint
from django.db.models import Sum




def orders(request):
    orders = Orders.objects.all()
    context = {
        "orders" : orders,
    }
    template = loader.get_template('order_base/orders.html')

    return HttpResponse(template.render(context, request))

def add_order(request):
    cs = Customer.objects.all()
    context = {
        'cs': cs
    }
    return render(request, 'order_base/add_order.html', context)

def insert_order(request):
    name = request.POST.get('order_name')
    c_id = request.POST.get('customer')
    quantity = request.POST.get('order_quantity')
    order = Orders()
    order.customer_id = c_id
    order.name = name
    order.quantity = quantity
    order.save()
    return redirect('orders')

def order_detail(request, order_id):
    order = Orders.objects.get(pk=order_id)
    template = loader.get_template('order_base/order_detail.html')
    context ={
        'order' : order
    }
    return HttpResponse(template.render(context, request))

def customer_detail(request, customer_id):
    orders = Orders.objects.filter(customer_id=customer_id)
    template = loader.get_template('order_base/customer_detail.html')
    order_numb = orders.aggregate(Sum("quantity"))
    context = {
        'orders' : orders,
        'order_numb' : order_numb,
    }
    return HttpResponse(template.render(context, request))

def edit_order(request, order_id):
    order = Orders.objects.get(pk=order_id)
    context ={
        'order' : order
    }
    template = loader.get_template('order_base/edit_order.html')
    return HttpResponse(template.render(context, request))

def update_order(request, order_id):
    order = Orders.objects.get(pk=order_id)
    name = request.POST.get('order_name')
    quantity = request.POST.get('order_quantity')
    order.name = name
    order.quantity = quantity
    order.save()
    return redirect('orders')

def delete_order(request, order_id):
    order = Orders.objects.filter(id=order_id).delete()
    return redirect('orders')

