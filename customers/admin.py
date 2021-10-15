from django.contrib import admin

from .models import Customer


class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "company",
        "first_name",
        "last_name",
        "accepted",
        "sales_contact",
    )


admin.site.register(Customer, CustomerAdmin)
