from .models import Customer
from .serializers import CustomerSerializer

from epicevents.permissions import IsAdmin, IsSaler
from events.models import Event

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet


class CustomerViewSet(ModelViewSet):
    """API endpoint that allows Customers to be viewed or edited."""

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated & (IsAdmin | IsSaler)]

    def perform_create(self, serializer, **kwargs):
        """Create a contract from a customer."""
        if self.request.user.role == "SALE":
            return serializer.save(sales_contact=self.request.user)
        else:
            return serializer.save()

    def list(self, request):
        """
        Get and display the list of contracts from a specific customer.
        Support users can only access to customers where they are event.support_contact.
        """
        user = self.request.user
        queryset = Customer.objects.all()
        if user.role == "SUPPORT":
            events = Event.objects.filter(support_contact=user)
            events_Customers = [event.customer.id for event in events]
            queryset = Customer.objects.filter(id__in=events_Customers)
        queryset = self.filter_queryset(queryset).order_by("company")
        serializer = CustomerSerializer(queryset, many=True)
        return Response(serializer.data)
