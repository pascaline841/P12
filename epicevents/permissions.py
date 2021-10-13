from rest_framework.permissions import BasePermission, SAFE_METHODS
from users.models import User


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        if request.user == "ADMIN":
            return request.method in ["POST"]
        else:
            return request.method in SAFE_METHODS

    def has_object_permission(self, request, view, obj):
        if request.user == "ADMIN":
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
    def has_permission(self, request, view):
        if request.user == "SALE":
            return request.method in ["POST"]
        else:
            return request.method in SAFE_METHODS

    def has_object_permission(self, request, view, obj):
        if request.user == "SALE":
            return request.method in ["GET", "PUT", "PATCH", "OPTIONS", "HEAD"]
        else:
            return request.method in SAFE_METHODS


class IsSalesContact(BasePermission):
    def has_permission(self, request, view):
        if request.user == "SALE":
            return request.method in ["POST"]
        else:
            return request.method in SAFE_METHODS

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
