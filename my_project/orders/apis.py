
from re import T
from rest_framework.response import Response
from .utils import getOrders
from rest_framework.decorators import api_view
from .models import Orders
from .serializers import OrderSerializer
from customer.models import Customer



@api_view(['GET'])
def api_orders(request):
    return getOrders(request)

@api_view(['GET'])
def order_detail(request, order_id):
    order = Orders.objects.get(pk=order_id)
    serializer = OrderSerializer(order, many=False)
    return Response(serializer.data)


@api_view(['POST'])  
def add_order(request):
    order = request.data
    new_order = Orders.objects.create(
        customer = Customer.objects.get(id=order["customer"]),
        name = order["name"],
        quantity = order["quantity"],
    )
    new_order.save()
    serializer = OrderSerializer(new_order)
    return Response(serializer.data)

@api_view(['POST'])
def edit_order(request, order_id):
    order = Orders.objects.get(pk=order_id)
    data = request.data
    customer = Customer.objects.get(id=data["customer"])
    order.customer = customer
    order.name = data["name"]
    order.quantity = data["quantity"]

    order.save()
    serializer = OrderSerializer(order)
    return Response(serializer.data)

@api_view(['GET'])
def customer_detail(request, customer_id):
    order = Orders.objects.filter(customer_id= customer_id)
    serializer = OrderSerializer(order, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def delete_order(request, order_id):
    order = Orders.objects.filter(id=order_id)
    order.delete()
    return Response({"order deleted!"})

