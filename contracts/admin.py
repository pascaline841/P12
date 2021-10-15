from .models import Contract

from django.contrib import admin


class ContractAdmin(admin.ModelAdmin):
    list_display = ("id", "customer", "signed", "sales_contact")


admin.site.register(Contract, ContractAdmin)
