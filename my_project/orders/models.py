from django.db import models
from customer.models import Customer

class Orders(models.Model):
    customer = models.ForeignKey(Customer,null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    quantity = models.IntegerField(default=0)
