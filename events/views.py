from .models import Event
from .serializers import EventSerializer

from contracts.models import Contract
from customers.models import Customer
from epicevents.permissions import IsAdmin, IsSalesContact, IsSupportContact

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet


class EventViewSet(ModelViewSet):
    """API endpoint that allows event to be viewed or edited."""

    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [
        IsAuthenticated & (IsAdmin | IsSalesContact | IsSupportContact)
    ]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filter_fields = [
        "sales_contact",
        "operational",
        "customer",
        "contract",
        "date",
        "support_contact",
        "guests",
    ]
    search_fields = [
        "sales_contact",
        "customer",
        "contract",
        "date",
        "support_contact",
    ]

    def perform_create(self, serializer, **kwargs):
        """Create an event."""
        customer = Customer.objects.get(pk=self.kwargs["customer_pk"])
        contract = Contract.objects.get(pk=self.kwargs["contract_pk"])
        contract.signed = True
        contract.save()
        serializer.save(
            customer=customer,
            contract=contract,
            sales_contact=contract.sales_contact,
        )

    def get_queryset(self, **kwargs):
        """
        Get and display the list of contracts from a specific customer.
        Support users can only access to event where they are event.support_contact.
        """
        user = self.request.user
        if user.role != "SUPPORT":
            return Event.objects.filter(contract=self.kwargs["contract_pk"])
        return Event.filter(contract=self.kwargs["contract_pk"], support_contact=user)
