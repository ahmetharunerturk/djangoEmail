from django import forms
from django.contrib.auth.models import User
from .models import EmailList

class EmailForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    email_list = forms.ModelChoiceField(queryset=EmailList.objects.all())
