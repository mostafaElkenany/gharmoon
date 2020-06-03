from django.urls import path
from .views import add_case

urlpatterns = [
    path('new', add_case, name='add_case'),
]