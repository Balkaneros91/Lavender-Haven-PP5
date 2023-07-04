from django.forms import ModelForm
from django import forms
from .models import ContactMessage


class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message_subject', 'message']

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter your name',
                                    'required': True}),
            'email': forms.EmailInput
            (attrs={'placeholder': 'Enter your email'}),

            'message_subject': forms.TextInput
            (attrs={'placeholder': 'Enter message title'}),

            'message': forms.TextInput
            (attrs={'placeholder': 'Enter your message'}),
        }
