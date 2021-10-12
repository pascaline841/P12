from rest_framework.permissions import BasePermission
from users.models import User


class IsAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ["PUT", "PATCH", "DELETE"]:
            admin_users = User.objects.filter(role="ADMIN")
            return request.user in admin_users.all()


class IsSaler(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ["PUT", "PATCH"]:
            saler_users = User.objects.filter(role="SALE")
            return request.user in saler_users.all()


class IsSalesContact(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ["PUT", "PATCH"]:
            return request.user == obj.sales_contact


class IsSupport(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ["PUT", "PATCH"]:
            return request.user == obj.support_contact
