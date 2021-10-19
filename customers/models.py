from django.conf import settings
from django.db import models


class Customer(models.Model):
    company = models.CharField(max_length=100)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=12, blank=True, null=True)
    social_media = models.CharField(max_length=100, blank=True, null=True)
    accepted = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True, null=True)
    sales_contact = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"{self.company}"
