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
            "message": forms.Textarea(attrs={"rows": 4}),
        }