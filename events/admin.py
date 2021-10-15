from .models import Event

from django.contrib import admin


class EventAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "contract",
        "customer",
        "operational",
        "sales_contact",
        "support_contact",
    )

    def active(self, obj):
        return obj.is_active == 1

    active.boolean = True


admin.site.register(Event, EventAdmin)
