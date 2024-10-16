import os
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.contrib import messages
from django.shortcuts import redirect, render
from .forms import ContactForm
from .models import Contact

def contact_us(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save the contact submission to the database
            contact_submission = Contact(
                name=form.cleaned_data["name"],
                email=form.cleaned_data["email"],
                phone_number=form.cleaned_data["phone_number"],
                subject=form.cleaned_data["subject"],
                message=form.cleaned_data["message"],
            )
            contact_submission.save()

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
            except Exception as e:
                messages.error(request, "Failed to send message to the property owner.")
                return redirect("contact_us")

            # Prepare the email to the user
            user_email = EmailMultiAlternatives(
                subject="Your Contact Form Submission",
                body=f"Dear {form.cleaned_data['name']},\n\n"
                     "Thank you for reaching out! Please find the attached brochure.\n\n"
                     "Best regards,\n"
                     "Your Company Name",
                from_email=None,  # Default from email
                to=[form.cleaned_data['email']],
            )

            # Path to the brochure file
            brochure_path = os.path.join(settings.BASE_DIR, 'staticfiles', 'files', 'brochure.pdf')
            # Check if the brochure file exists before attaching it
            if os.path.exists(brochure_path):
                user_email.attach_file(brochure_path)  # Attach the PDF

            # Send the email to the user
            try:
                user_email.send()
            except Exception as e:
                messages.error(request, "Failed to send the brochure to your email.")
                return redirect("contact_us")

            messages.success(request, "Thank you for submitting! We will be in touch soon!")
            return redirect("contact_us")

    else:
        form = ContactForm()

    return render(request, "contact.html", {"form": form})
