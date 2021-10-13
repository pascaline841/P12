from .models import Customer
from users.models import User
from rest_framework.serializers import ModelSerializer, ChoiceField


class CustomerSerializer((ModelSerializer)):
    class Meta:
        model = Customer
        fields = "__all__"
        read_only_fields = ["date_created", "date_update"]
