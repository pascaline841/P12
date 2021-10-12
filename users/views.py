from .models import User
from .serializers import UserSerializer

from epicevents.permissions import IsAdmin

from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet


class UserViewSet(ModelViewSet):
    """
    API endpoint that allows Users to be viewed or edited.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated & IsAdmin]

    def get_queryset(self, **kwargs):
        """Get and display the list of contracts from a specific customer."""
        admin_users = User.objects.filter(role="ADMIN")
        if self.request.user in admin_users.all():
            return User.objects.all()
        else:
            return User.objects.filter(username=self.request.user)
