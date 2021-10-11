from .models import Event

from rest_framework.serializers import ModelSerializer


class EventSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"
        read_only_fields = [
            "customer",
            "contract",
            "date_created",
            "date_update",
            "sales_contact",
        ]
