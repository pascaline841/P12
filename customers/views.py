from users.models import User
from .models import Customer
from .serializers import CustomerSerializer

from epicevents.permissions import IsAdmin, IsSaler

from rest_framework.permissions import IsAuthenticated
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
