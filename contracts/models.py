from customers.models import Customer

from django.conf import settings
from django.db import models


class Contract(models.Model):

    signed = models.BooleanField(default=False)
    amount = models.FloatField(null=True)
    payement_due = models.DateField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True, null=True)
    sales_contact = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    customer = models.ForeignKey(
        to=Customer,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"{self.id}"
