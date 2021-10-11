from contracts.models import Contract
from customers.models import Customer

from django.conf import settings
from django.db import models


class Event(models.Model):

    customer = models.ForeignKey(
        to=Customer,
        on_delete=models.CASCADE,
        related_name="customer",
        blank=True,
        null=True,
    )
    contract = models.OneToOneField(
        to=Contract,
        on_delete=models.CASCADE,
        related_name="contract",
        blank=True,
        null=True,
    )
    date = models.DateField(blank=True, null=True)
    guests = models.IntegerField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True, null=True)
    operational = models.BooleanField(default=False)
    sales_contact = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="sales_contact",
        blank=True,
        null=True,
    )
    support_contact = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="support_contact",
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"N° {self.id} - {self.customer}"
