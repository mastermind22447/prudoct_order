
from rest_framework.response import Response
from .models import Customer
from .serialiser import CustomerSerializer

def getCustomers(request):
    customer = Customer.objects.all()
    serializer = CustomerSerializer(customer, many= True)
    return Response(serializer.data)