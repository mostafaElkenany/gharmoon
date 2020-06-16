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
            "governerate",
            "jail_name",
            "convection_date",
            "jail_time",
            "no_of_dependents",
            "total_target",
            "details",
        )

        error_messages = {
            'total_target': {
                'min_value': "Total target must be greater than zero",
            },
            'jail_time': {
                'min_value': "jail time must be greater than or equal to one year",
            },
            'no_of_dependents': {
                'min_value': "Number of dependents must be greater than or equal to zero",
            },
            'age': {
                'min_value': "Age must be 18 or above",
            },
        }

        widgets = {
            "convection_date": forms.DateInput(attrs={"type": "date"}),
        }
        
    def clean(self):
        cleaned_data = super().clean()
        convection_date = cleaned_data.get("convection_date")
        if convection_date :
            if convection_date > datetime.date.today():
                msg = "Convection date should be before or equal current date."
                self.add_error("convection_date", msg)

class SearchCaseForm(forms.ModelForm):
    
    GENDER = Case.GENDER_CHOICES
    GENDER = (('', '----'),) + GENDER

    GOVERNRATES = Case.GOVERNRATES
    GOVERNRATES = (('', '----'),) + GOVERNRATES
    
    name = forms.CharField(required=False)
    gender = forms.ChoiceField(required=False, choices=GENDER)
    governerate = forms.ChoiceField(required=False, choices=GOVERNRATES)
    jail_name = forms.CharField(required=False)
    jail_time = forms.IntegerField(required=False)
    no_of_dependents = forms.IntegerField(required=False)
    total_target = forms.IntegerField(required=False)
    
    class Meta:
        model = Case
        fields = (
        "name",
        "gender",
        "governerate",
        "jail_name",
        "jail_time",
        "no_of_dependents",
        "total_target",
        )
        
