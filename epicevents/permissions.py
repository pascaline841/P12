from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdmin(BasePermission):
    """
    Only allow user.role= ADMIN to access to all permissions to all objects and users.
    """

    def has_permission(self, request, view):
        if request.user.role == "ADMIN":
            return True
        else:
            return request.method in SAFE_METHODS

    def has_object_permission(self, request, view, obj):
        if request.user.role == "ADMIN":
            return True
        else:
            return request.method in SAFE_METHODS


class IsSaler(BasePermission):
    """
    Allow user.role = SALE to POST, GET customer or contracts or events.
    """

    def has_permission(self, request, view):
        if request.user.role == "SALE":
            return request.method in ["POST", "GET", "PUT", "PATCH", "OPTIONS", "HEAD"]
        else:
            return request.method in SAFE_METHODS

    def has_object_permission(self, request, view, obj):
        if request.user.role == "SALE":
            return request.method in ["GET", "PUT", "PATCH", "OPTIONS", "HEAD"]
        else:
            return request.method in SAFE_METHODS


class IsSalesContact(BasePermission):
    """Allow user to PATCH, PUT if contract.sales_contact == user."""

    def has_permission(self, request, view):
        if request.user.role == "SALE":
            return request.method in ["POST", "GET", "PUT", "PATCH", "OPTIONS", "HEAD"]
        else:
            return request.method in SAFE_METHODS

    def has_object_permission(self, request, view, obj):
        if request.user == obj.sales_contact:
            return request.method in ["GET", "PUT", "PATCH", "OPTIONS", "HEAD"]
        else:
            return request.method in SAFE_METHODS


class IsSupportContact(BasePermission):
    """Allow user to PATCH, PUT if contract.support_contact == user."""

    def has_object_permission(self, request, view, obj):
        if request.user == obj.support_contact:
            return request.method in ["GET", "PUT", "PATCH", "OPTIONS", "HEAD"]
        else:
            return request.method in SAFE_METHODS
