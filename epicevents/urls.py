"""epicevents URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from contracts.views import ContractViewSet
from customers.views import CustomerViewSet
from events.views import EventViewSet
from users.views import UserViewSet

from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedSimpleRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


router = DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r"customers", CustomerViewSet)

customer_router = NestedSimpleRouter(router, r"customers", lookup="customer")
customer_router.register(r"contracts", ContractViewSet, basename="contract")

contract_router = NestedSimpleRouter(customer_router, r"contracts", lookup="contract")
contract_router.register(r"events", EventViewSet, basename="event")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("", include(customer_router.urls)),
    path("", include(contract_router.urls)),
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
