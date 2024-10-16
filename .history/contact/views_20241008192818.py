import os
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.shortcuts import redirect, render

from .forms import ContactForm
from .models import Contact


def contact_us(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # Create a new Contact instance and save the data, including the phone number
            contact_submission = Contact(
                name=form.cleaned_data["name"],
                email=form.cleaned_data["email"],
                phone_number=form.cleaned_data["phone_number"],  # Save the phone number
                subject=form.cleaned_data["subject"],
                message=form.cleaned_data["message"],
            )
            contact_submission.save()  # Save the data to the database

            # Prepare the email details
            email_subject = form.cleaned_data["subject"]
            email_message = (
                f"Message from {form.cleaned_data['name']} "
                f"<{form.cleaned_data['email']}>\n\n"
                f"Phone: {form.cleaned_data['phone_number']}\n\n"  # Include phone number
                f"{form.cleaned_data['message']}"
            )

            # Prepare the brochure path
            brochure_path = os.path.join(settings.BASE_DIR, 'staticfiles', 'files', 'brochure.pdf')

            # Send the email
            email = EmailMessage(
                subject=email_subject,
                body=email_message,
                from_email=None,  # Use default from email
                to=[os.environ.get("CONTACT_EMAIL_RECIPIENT")],
            )
            email.attach_file(brochure_path)  # Attach the PDF

            # Send the email with the attachment
            email.send(fail_silently=False)

            # Optionally, send a confirmation email to the user (including the brochure)
            user_email = form.cleaned_data["email"]
            confirmation_email = EmailMessage(
                subject="Your Inquiry Confirmation",
                body=f"Dear {form.cleaned_data['name']},\n\nThank you for contacting us! "
                      f"We have received your message and will get back to you shortly.\n\n"
                      f"Best regards,\nYour Team",
                from_email=None,  # Use default from email
                to=[user_email],
            )
            confirmation_email.attach_file(brochure_path)  # Attach the PDF brochure for the user
            confirmation_email.send(fail_silently=False)

            messages.success(request, "Thank you for submitting! We will be in touch soon!")
            return redirect("contact_us")

    else:
        form = ContactForm()

    return render(request, "contact.html", {"form": form})
