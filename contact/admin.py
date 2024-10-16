from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "email",
        "phone_number",  # Added phone_number to list display
        "subject",
        "created_at",
    )

    search_fields = (
        "name",
        "email",
        "phone_number",  # Added phone_number to search fields
        "subject",
        "message",
    )

    list_filter = (
        "subject",
        "created_at",
    )

    ordering = ("-created_at",)  # Order by creation date in descending order

    # Customize the form layout
    fieldsets = (
        (None, {"fields": ("name", "email", "phone_number", "subject", "message", "created_at")}),  # Included phone_number
    )

    readonly_fields = ("created_at",)  # Make 'created_at' read-only
