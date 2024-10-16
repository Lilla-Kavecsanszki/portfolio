import os
from django.core.mail import send_mail, EmailMessage
from django.shortcuts import redirect, render
from django.contrib import messages
from django.templatetags.static import static

from .forms import ContactForm
from .models import Contact
from django.conf import settings

def contact_us(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            contact_submission = Contact(
                name=form.cleaned_data["name"],
                email=form.cleaned_data["email"],
                phone_number=form.cleaned_data["phone_number"],
                subject=form.cleaned_data["subject"],
                message=form.cleaned_data["message"],
            )
            contact_submission.save()

            # Send mail to the site owner
            send_mail(
                form.cleaned_data["subject"],  # subject
                f"Message from {form.cleaned_data['name']} "
                f"<{form.cleaned_data['email']}>\n\n"
                f"Phone: {form.cleaned_data['phone_number']}\n\n"
                f"{form.cleaned_data['message']}",  # message body
                None,  # from email (default from settings)
                [os.environ.get("CONTACT_EMAIL_RECIPIENT")],  # to site owner
            )

            # Prepare to send a confirmation email to the user with the brochure
            user_email = form.cleaned_data['email']
            subject = "Thank you for contacting us!"
            message = (
                f"Dear {form.cleaned_data['name']},\n\n"
                "Thank you for getting in touch with us. Attached is the brochure you requested."
            )
            
            # Create an email message
            email = EmailMessage(
                subject=subject,
                body=message,
                from_email=settings.DEFAULT_FROM_EMAIL,  # Assuming you have this set up in settings.py
                to=[user_email],
            )

            # Attach the PDF brochure (Ensure the file exists in the 'static' or 'media' folder)
            brochure_path = os.path.join(settings.BASE_DIR, src="{% static 'images/brochure.png' %}")  # Replace with actual path
            email.attach_file(brochure_path)  # Attach the PDF

            # Send the email to the user
            email.send()

            # Inform the user the form was submitted successfully
            messages.success(request, "Thank you for submitting! We will be in touch soon, and the brochure has been sent to your email.")

            return redirect("contact_us")  # Redirect to the contact page after success

    else:
        form = ContactForm()

    return render(request, "contact.html", {"form": form})
