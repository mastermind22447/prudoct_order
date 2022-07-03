from django.db import models
from customer.models import Customer

class Orders(models.Model):
    customer = models.ForeignKey(Customer, related_name='customer_order', null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return str(self.name)
