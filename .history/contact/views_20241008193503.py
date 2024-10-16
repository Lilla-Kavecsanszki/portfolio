import os
from django.conf import settings
from django.contrib import messages
from django.core.mail import EmailMessage
from django.shortcuts import redirect, render

from .forms import ContactForm
from .models import Contact

def contact_us(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_submission = Contact(
                name=form.cleaned_data["name"],
                email=form.cleaned_data["email"],
                phone_number=form.cleaned_data["phone_number"],  # Save phone number
                subject=form.cleaned_data["subject"],
                message=form.cleaned_data["message"],
            )
            contact_submission.save()  # Save the data to the database

            # Prepare the email to the property owner
            owner_email = EmailMessage(
                subject=form.cleaned_data["subject"],
                body=f"Message from {form.cleaned_data['name']} "
                     f"<{form.cleaned_data['email']}>\n\n"
                     f"Phone: {form.cleaned_data['phone_number']}\n\n"
                     f"{form.cleaned_data['message']}",
                from_email=None,  # Default from email
                to=[os.environ.get("CONTACT_EMAIL_RECIPIENT")],
            )

            # Send the email to the property owner
            owner_email.send()

            # Prepare the email to the user
            user_email = EmailMessage(
                subject="Your Contact Form Submission",
                body=f"Dear {form.cleaned_data['name']},\n\n"
                     "Thank you for reaching out! Please find the attached brochure.\n\n"
                     "Best regards,\n"
                     "Your Company Name",  # Replace with your company name
                from_email=None,  # Default from email
                to=[form.cleaned_data['email']],
            )

            # Path to the brochure
            brochure_path = os.path.join(settings.BASE_DIR, 'static', 'files', 'brochure.pdf')
            user_email.attach_file(brochure_path)  # Attach the PDF

            # Send the email to the user
            user_email.send()

            messages.success(request, "Thank you for submitting! We will be in touch soon!")
            return redirect("contact_us")

    else:
        form = ContactForm()

    return render(request, "contact.html", {"form": form})
