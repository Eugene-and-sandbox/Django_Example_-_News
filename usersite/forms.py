from django import forms


class ContactForm(forms.Form):
    subject = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}))
    message = forms.CharField(label='', widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write your message and contact information for feedback', 'rows': 5}))
