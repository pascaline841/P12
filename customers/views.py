from .models import Customer
from .serializers import CustomerSerializer

from epicevents.permissions import IsAdmin, IsSaler

from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet


class CustomerViewSet(ModelViewSet):
    """API endpoint that allows Customers to be viewed or edited."""

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [(IsAuthenticated & IsAdmin) | (IsAuthenticated & IsSaler)]
