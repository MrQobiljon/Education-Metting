from django import forms
from .models import Message


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('name', 'mail', 'subject', 'message')

        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': "YOURNAME...*"
            }),
            'mail': forms.EmailInput(attrs={
                'placeholder': "YOUR EMAIL..."
            }),
            'subject': forms.TextInput(attrs={
                'placeholder': "SUBJECT...*"
            }),
            'message': forms.Textarea(attrs={
                'placeholder': "YOUR MESSAGE...",
                'class': "form-control"
            })
        }