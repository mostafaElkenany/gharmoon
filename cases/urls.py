from django.urls import path
from .views import add_case, show_cases

urlpatterns = [
    path('new', add_case, name='add_case'),
    path('', show_cases, name='show_cases')
]