from .models import Customer

from rest_framework.serializers import ModelSerializer


class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"
        read_only_fields = ["date_created", "date_update", "sales_contact"]

    def create(self, validated_data):
        """Function to create a new customer."""
        new_customer = Customer.objects.create(**validated_data)
        new_customer.sales_contact = self.context["request"].user
        new_customer.save()
        return new_customer
