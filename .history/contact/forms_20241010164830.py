from django import forms
from phonenumber_field.formfields import PhoneNumberField
from .models import Contact

class ContactForm(forms.ModelForm):
    phone_number = PhoneNumberField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Phone number (+39 333 123 4567)'})  # Italian placeholder example
    )

    class Meta:
        model = Contact
        fields = ["name", "email", "phone_number", "subject", "message"]
        widgets = {
            "name": forms.TextInput(attrs={'placeholder': 'Name'}),  # Placeholder for name
            "email": forms.EmailInput(attrs={'placeholder': 'Email Address'}),  # Placeholder for email
            "subject": forms.TextInput(attrs={'placeholder': 'I would like to ask about...'}),  # Placeholder for subject
            "message": forms.Textarea(attrs={
                "rows": 4,
                'placeholder': 'Your Message'  # Placeholder for message
            }),
        }
