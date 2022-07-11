from rest_framework.response import Response
from .models import Orders
from .serializers import OrderSerializer

def getOrders(request):
    orders = Orders.objects.all()
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)