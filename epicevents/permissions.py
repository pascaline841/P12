from rest_framework.permissions import BasePermission, SAFE_METHODS
from users.models import User


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == "ADMIN"

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return request.user.role == "ADMIN"


class IsSaler(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == "SALE"

    def has_object_permission(self, request, view, obj):
        if request.user.role == "SALE":
            return request.method in ["GET", "PUT", "PATCH", "OPTIONS", "HEAD"]
        else:
            return request.method in SAFE_METHODS


class IsSalesContact(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == "SALE"

    def has_object_permission(self, request, view, obj):
        if request.user == obj.sales_contact:
            return request.method in ["GET", "PUT", "PATCH", "OPTIONS", "HEAD"]
        else:
            return request.method in SAFE_METHODS


class IsSupportContact(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user == obj.support_contact:
            return request.method in ["GET", "PUT", "PATCH", "OPTIONS", "HEAD"]
        else:
            return request.method in SAFE_METHODS
