from django.contrib import admin

from .models import Property, PropertyImage, PropertyVideo


class PropertyImageInline(admin.TabularInline):
    model = PropertyImage
    extra = 1  # Number of extra forms to display for adding images


class PropertyVideoInline(admin.TabularInline):
    model = PropertyVideo
    extra = 1  # Number of extra forms to display for adding videos


class PropertyAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "location",
        "property_type",
        "price",
        "size",
        "bedrooms",
        "bathrooms",
        "created_at",
        "number_of_likes",
    )
    list_filter = ("location", "property_type", "bedrooms", "bathrooms", "created_at")
    search_fields = ("name", "description", "location", "property_type")
    ordering = ("-created_at",)
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "name",
                    "description",
                    "features",
                    "location",
                    "property_type",
                    "price",
                    "size",
                )
            },
        ),
        ("Media", {"fields": ("main_image", "main_video")}),
        ("Details", {"fields": ("bedrooms", "bathrooms")}),
        (
            "Likes",
            {
                "fields": ("liked_by",),
                "classes": ("collapse",),  # This hides the fieldset by default
            },
        ),
    )
    inlines = [
        PropertyImageInline,
        PropertyVideoInline,
    ]  # Add this line to include inlines

    def number_of_likes(self, obj):
        return obj.number_of_likes()

    number_of_likes.short_description = "Number of Likes"


# Register the model with the customized admin
admin.site.register(Property, PropertyAdmin)
