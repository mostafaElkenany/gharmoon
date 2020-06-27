from django import forms
from tinymce.widgets import TinyMCE


class ContactForm(forms.Form):
    subject= forms.CharField(max_length=50, label="subject")
    email= forms.EmailField(max_length=50, label="Email")
    comment= forms.CharField(widget=TinyMCE())
    
