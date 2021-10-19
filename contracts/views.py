from .models import Contract
from .serializers import ContractSerializer

from customers.models import Customer
from epicevents.permissions import IsAdmin, IsSalesContact
from events.models import Event

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet


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
        if self.request.user.role == "SALE":
            contract = serializer.save(
                customer=customer, sales_contact=self.request.user
            )
        else:
            contract = serializer.save(
                customer=customer, sales_contact=customer.sales_contact
            )
        if contract.signed == True:
            Event.objects.create(
                contract=contract,
                customer=contract.customer,
                sales_contact=contract.sales_contact,
            )

    def list(self, request, **kwargs):
        """
        Get and display the list of contracts from a specific customer.
        Support users can only access to contract where they are event.support_contact.
        """
        user = self.request.user
        queryset = Contract.objects.filter(customer=self.kwargs["customer_pk"])
        if user.role == "SUPPORT":
            events = Event.objects.filter(support_contact=user)
            events_contracts = [event.contract.id for event in events]
            queryset = Contract.objects.filter(id__in=events_contracts)
        queryset = self.filter_queryset(queryset).order_by("date_update")
        serializer = ContractSerializer(queryset, many=True)
        return Response(serializer.data)
