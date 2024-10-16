from django.shortcuts import render

from properties.models import Property


def homepage(request):
    """Fetch properties or other data to pass to the template."""
    properties = Property.objects.all()  # Fetch all properties

    context = {
        "property_list": properties,  # Pass properties to the template
    }

    return render(request, "index.html", context)


def property_list_view(request):
    properties = Property.objects.all()  # Fetch all properties
    return render(request, "your_template.html", {"property_list": properties})