from django.shortcuts import render, redirect
from django.core.mail import EmailMultiAlternatives
from django.contrib import messages
import os
from django.conf import settings
from .forms import ContactForm

def homepage(request):
    """Handle contact form submissions and render the homepage."""
    form = ContactForm()  # Initialize the contact form

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save the contact submission to the database
            form.save()

            # Prepare the email to the property owner
            owner_email = EmailMultiAlternatives(
                subject=form.cleaned_data["subject"],
                body=f"Message from {form.cleaned_data['name']} "
                     f"<{form.cleaned_data['email']}>\n\n"
                     f"Phone: {form.cleaned_data['phone_number']}\n\n"
                     f"{form.cleaned_data['message']}",
                from_email=None,  # Default from email
                to=[os.environ.get("CONTACT_EMAIL_RECIPIENT")],
            )
            try:
                owner_email.send()
            except Exception:
                messages.error(request, "Failed to send message to the property owner.")
                return redirect("home")  # Redirect if email fails

            messages.success(request, "Thank you for submitting! We will be in touch soon!")
            return redirect("home")  # Redirect after successful submission

    return render(request, "index.html", {"form": form})  # Render the homepage template