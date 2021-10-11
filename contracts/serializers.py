from .models import Contract


from rest_framework.serializers import ModelSerializer


class ContractSerializer(ModelSerializer):
    class Meta:
        model = Contract
        fields = "__all__"
        read_only_fields = ["customer", "date_created", "date_update"]
