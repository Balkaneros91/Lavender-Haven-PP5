from django.forms import ModelForm
from django import forms
from .models import Testimonials


class TestimonialsForm(forms.ModelForm):
    class Meta:
        model = Testimonials
        fields = ['name', 'email', 'testimonial']

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter your name',
                                    'required': True}),
            'email': forms.EmailInput
            (attrs={'placeholder': 'Enter your email'}),
            'testimonial': forms.Textarea
            (attrs={'rows': 2, 'placeholder': 'Type here your testimonial'}),
        }
