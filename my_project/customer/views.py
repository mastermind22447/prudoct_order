from django.shortcuts import render, redirect
import customer
from .models import Customer
from django.http import HttpResponse
from django.template import loader

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
    customer = Customer.objects.get(pk=customer_id)
    template = loader.get_template('customer_base/customer_detail.html')
    context = {
        'customer' : customer
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