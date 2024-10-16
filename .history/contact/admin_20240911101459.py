from django.contrib import admin

from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "email",
        "subject",
        "created_at",
    )  # Include created_at in the list display

    search_fields = (
        "name",
        "email",
        "subject",
        "message",
    )  # Added 'message' for searching

    list_filter = (
        "subject",
        "created_at",
    )  # Added 'created_at' for filtering by date

    ordering = ("-created_at",)  # Order by creation date in descending order

    # Optional: Customize the form layout
    fieldsets = (
        (None, {"fields": ("name", "email", "subject", "message", "created_at")}),
    )

    readonly_fields = ("created_at",)  # Make 'created_at' read-only
