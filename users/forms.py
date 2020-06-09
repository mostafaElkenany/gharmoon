from django import forms
from .models import User
from django.contrib.auth.hashers import check_password


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "mobile_phone",
            "profile_picture",
        )


class ConfirmPasswordForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ("password",)
        labels = {"confirm_password": "Password"}
    
    def clean(self):
        cleaned_data = super(ConfirmPasswordForm, self).clean()
        confirm_password = cleaned_data.get("password")
        if not check_password(confirm_password, self.instance.password):
            self.add_error("password", "Password does not match.")
