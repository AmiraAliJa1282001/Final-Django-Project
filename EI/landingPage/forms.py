from django import forms
from .models import ContactMessages
class ContactMessagesForm(forms.ModelForm):
    full_name = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(
        attrs={
        "placeholder": "Enter your full name...",
        "class": "  form-control mb-1 p-3",
        "style":" height:100%"
        }
        ),
        label="",
         max_length=500
    )
    email = forms.EmailField(
        required=True,
        widget=forms.widgets.TextInput(
        attrs={
        "placeholder": "Enter your email...",
        "class": "form-control mb-1 p-3",
        }
        ),
        label="",
         max_length=500
    )
    message_content = forms.CharField(
        required=True,
        widget=forms.widgets.Textarea(
        attrs={
        "placeholder": "Enter your message...",
        "class": "form-control mb-1 p-3 ",
        }
        ),
        label="",
         max_length=500
    )
    class Meta:
        model = ContactMessages
        exclude = ("user", )