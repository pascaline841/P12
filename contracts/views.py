from .models import Contract
from .serializers import ContractSerializer

from customers.models import Customer
from epicevents.permissions import IsAdmin, IsSalesContact
from events.models import Event

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet


class ContractViewSet(ModelViewSet):
    """API endpoint that allows contract to be viewed or edited."""

    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    permission_classes = [IsAuthenticated & (IsAdmin | IsSalesContact)]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filter_fields = ["sales_contact", "signed", "amount", "payement_due"]
    search_fields = [
        "sales_contact",
    ]

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

    def get_queryset(self, **kwargs):
        """
        Get and display the list of contracts from a specific customer.
        Support users can only access to contract where they are event.support_contact.
        """
        user = self.request.user
        if user.role != "SUPPORT":
            return Contract.objects.filter(customer=self.kwargs["customer_pk"])
        events = Event.objects.filter(support_contact=user)
        events_contracts = [event.contract.id for event in events]
        return Contract.objects.filter(
            customer=self.kwargs["customer_pk"], id__in=events_contracts
        )
