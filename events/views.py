from .models import Event
from .serializers import EventSerializer

from contracts.models import Contract
from customers.models import Customer
from epicevents.permissions import IsAdmin, IsSalesContact, IsSupport

from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet


class EventViewSet(ModelViewSet):
    """API endpoint that allows event to be viewed or edited."""

    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [
        (IsAuthenticated & IsAdmin)
        | (IsAuthenticated & IsSalesContact)
        | (IsAuthenticated & IsSupport)
    ]

    def perform_create(self, serializer, **kwargs):
        """Create an event."""
        customer = Customer.objects.get(pk=self.kwargs["customer_pk"])
        contract = Contract.objects.get(pk=self.kwargs["contract_pk"])
        sales_contact = self.request.user
        serializer.save(
            customer=customer, contract=contract, sales_contact=sales_contact
        )

    def get_queryset(self, **kwargs):
        """Get and display the list of events from a specific contract."""
        return Event.objects.filter(contract=self.kwargs["contract_pk"])
