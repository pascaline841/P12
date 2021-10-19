from .models import Customer
from rest_framework.serializers import ModelSerializer


class CustomerSerializer((ModelSerializer)):
    class Meta:
        model = Customer
        fields = "__all__"
        read_only_fields = ["date_created", "date_update"]
