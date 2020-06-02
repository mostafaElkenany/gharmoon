from django.contrib.auth.forms import UserCreationForm
from users.models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta():
        model = User
        fields = UserCreationForm.Meta.fields
        fields += (
            "email",
            "first_name",
            "last_name",
            "mobile_phone",
            "profile_picture",
            )
