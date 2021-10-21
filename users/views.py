from .models import User
from .serializers import UserSerializer

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet


class UserViewSet(ModelViewSet):
    """
    API endpoint that allows Users to be viewed or edited.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filter_fields = ["role"]
    search_fields = [
        "first_name",
        "last_name",
        "email",
        "username",
    ]
    '''
    def get_queryset(self, **kwargs):
        """Get and display the list of contracts from a specific customer."""
        admin_users = User.objects.filter(role="ADMIN")
        if self.request.user in admin_users.all():
            return User.objects.all()
        else:
            return User.objects.filter(username=self.request.user)
    '''
