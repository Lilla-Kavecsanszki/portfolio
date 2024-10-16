from django import forms
from phonenumber_field.formfields import PhoneNumberField
from .models import Contact

class ContactForm(forms.ModelForm):
    phone_number = PhoneNumberField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'es. +39 333 123 4567'})  # Italian placeholder example
    )

    class Meta:
        model = Contact
        fields = ["name", "email", "phone_number", "subject", "message"]
        widgets = {
            "name": forms.TextInput(attrs={'placeholder': 'Your Name'}),  # Placeholder for name
            "email": forms.EmailInput(attrs={'placeholder': 'Your Email'}),  # Placeholder for email
            "subject": forms.TextInput(attrs={'placeholder': 'Subject'}),  # Placeholder for subject
            "message": forms.Textarea(attrs={
                "rows": 4,
                'placeholder': 'Your Message'  # Placeholder for message
            }),
        }
