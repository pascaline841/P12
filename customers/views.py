from .models import Customer
from .serializers import CustomerSerializer

from epicevents.permissions import IsAdmin, IsSaler
from events.models import Event

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter


class CustomerViewSet(ModelViewSet):
    """API endpoint that allows Customers to be viewed or edited."""

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated & (IsAdmin | IsSaler)]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filter_fields = ["sales_contact", "accepted", "customer"]
    search_fields = [
        "first_name",
        "last_name",
        "company",
        "email",
        "phone",
        "sales_contact",
    ]

    def perform_create(self, serializer, **kwargs):
        """Create a contract from a customer."""
        if self.request.user.role == "SALE":
            return serializer.save(sales_contact=self.request.user)
        else:
            return serializer.save()

    def get_queryset(self, **kwargs):
        """Get and display the list of contracts from a specific customer."""
        user = self.request.user
        if user.role != "SUPPORT":
            return Customer.objects.all()
        events = Event.objects.filter(support_contact=user)
        events_Customers = [event.customer.id for event in events]
        return Customer.objects.filter(id__in=events_Customers)
