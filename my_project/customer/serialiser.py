from pyexpat import model
from rest_framework.serializers import ModelSerializer
from dataclasses import field
from .models import Customer

class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'