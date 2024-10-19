from django.shortcuts import render

# Define the 'index' view for the 'projects' app
def index(request):
    # You can render a template here or return an HTTP response
    return render(request, 'projects/index.html')  # Replace with the actual template path
