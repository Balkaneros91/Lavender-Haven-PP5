from django.forms import ModelForm
from django import forms
from .models import ContactMessage, Newsletter


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


class UpdateNewsletter(ModelForm):
    class Meta:
        model = Newsletter
        fields = ['email']

    def __init__(self, *args, **kwargs):
        super(UpdateNewsletter, self).__init__(*args, **kwargs)

        self.fields['email'].widget.attrs.update(
            {'class': 'form-control',
             'placeholder': 'Enter your Email...'})
