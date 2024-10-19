from django.shortcuts import render

def homepage(request):
    context = {}  # Define an empty context dictionary
    return render(request, "index.html", context)
