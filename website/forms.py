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
        fields = ["name", "surname", "email", "phone_number", "subject", "message"]
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Your First Name"}),
            "surname": forms.TextInput(attrs={"placeholder": "Your Last Name"}),
            "email": forms.EmailInput(attrs={"placeholder": "Your Email Address"}),
            "phone_number": forms.TextInput(attrs={"placeholder": "e.g. +39 333 123 4567"}),  # Placeholder example for Italian number
            "subject": forms.TextInput(attrs={"placeholder": "Subject"}),
            "message": forms.Textarea(attrs={"rows": 4, "placeholder": "Your Message"}),
        }