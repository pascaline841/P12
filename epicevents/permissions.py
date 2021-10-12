from rest_framework.permissions import BasePermission, SAFE_METHODS
from users.models import User


class IsAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        admin_users = User.objects.filter(role="ADMIN")
        if request.user in admin_users.all():
            return request.method in [
                "GET",
                "PUT",
                "PATCH",
                "OPTIONS",
                "HEAD",
                "DELETE",
            ]
        else:
            return request.method in SAFE_METHODS


class IsSaler(BasePermission):
    def has_object_permission(self, request, view, obj):
        sale_users = User.objects.filter(role="SALE")
        if request.user in sale_users.all():
            return request.method in ["GET", "PUT", "PATCH", "OPTIONS", "HEAD"]
        else:
            return request.method in SAFE_METHODS


class IsSalesContact(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ["PUT", "PATCH"]:
            return request.user == obj.sales_contact


class IsSupport(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ["PUT", "PATCH"]:
            return request.user == obj.support_contact
