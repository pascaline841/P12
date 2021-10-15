from django.contrib import admin

from .models import User


class UsersAdmin(admin.ModelAdmin):
    list_display = ("username", "first_name", "last_name", "role")


admin.site.site_header = "EPIC EVENTS CRM"
admin.site.register(User, UsersAdmin)
