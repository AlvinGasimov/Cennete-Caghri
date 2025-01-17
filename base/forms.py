from django import forms
from .models import Subscribe
from .models import Contact

class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscribe
        fields = ['email']
        widgets = {
            "email": forms.EmailInput(
                attrs={
                    "placeholder": "Mail Adresinizi Girin",
                }
            )
        }

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'İsim ve Soyisminiz',
                'class': 'form-control mb-3'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Mail Adresiniz',
                'class': 'form-control mb-3'
            }),
            'phone': forms.TextInput(attrs={
                'placeholder': 'Telefon Numarası',
                'class': 'form-control mb-3 phone-mask',
            }),
            'subject': forms.TextInput(attrs={
                'placeholder': 'Mesajın Konusu',
                'class': 'form-control mb-3'
            }),
            'message': forms.Textarea(attrs={
                'placeholder': 'Mesajınız',
                'class': 'form-control mb-3'
            })
        }
