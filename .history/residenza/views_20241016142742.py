from django.shortcuts import render

from properties.models import Property


def homepage(request):
  

    return render(request, "index.html", context)