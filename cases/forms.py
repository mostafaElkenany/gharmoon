from django import forms
from .models import Case
import datetime

class AddCaseForm(forms.ModelForm):
    class Meta:
        model = Case
        fields = (
            "name",
            "national_id",
            "gender",
            "age",
            "jail_name",
            "governerate",
            "convection_date",
            "jail_time",
            "no_of_dependents",
            "total_target",
            "details",
        )
        error_messages = {
            'total_target': {
                'min_value': "Invalid value, target must be greater than zero",
            },
        }
