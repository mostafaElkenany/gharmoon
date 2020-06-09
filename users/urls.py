from django.urls import path
from .views import show_profile, get_cases, get_donations, edit_profile, change_password,delete_account

urlpatterns = [
    path('', show_profile, name='profile'),
    path('edit', edit_profile, name='edit_profile'),
    path('password', change_password, name='change_password'),
    path('profile/delete', delete_account, name='delete_account'),
    path('user/cases', get_cases , name='user_cases'),
    path('user/donations', get_donations , name='user_donations'),

]