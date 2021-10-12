from .models import Contract
from .serializers import ContractSerializer

from customers.models import Customer
from epicevents.permissions import IsAdmin, IsSalesContact
from events.models import Event

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated


class ContractViewSet(ModelViewSet):
    """API endpoint that allows contract to be viewed or edited."""

    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    permission_classes = [IsAuthenticated & (IsAdmin | IsSalesContact)]

    def perform_create(self, serializer, **kwargs):
        """Create a contract from a customer."""
        customer = Customer.objects.get(pk=self.kwargs["customer_pk"])
        customer.accepted = True
        customer.save()
        contract = serializer.save(customer=customer, sales_contact=self.request.user)
        if contract.signed == True:
            Event.objects.create(
                contract=contract,
                customer=contract.customer,
                sales_contact=self.request.user,
            )

    def get_queryset(self, **kwargs):
        """Get and display the list of contracts from a specific customer."""
        return Contract.objects.filter(customer=self.kwargs["customer_pk"])
