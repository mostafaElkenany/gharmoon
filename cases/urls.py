from django.urls import path
from .views import add_case, show_cases, search_cases, search

urlpatterns = [
    path('new', add_case, name='add_case'),
    path('', show_cases, name='show_cases'),
    path('search', search, name='search'),
    path('results', search_cases, name='search_cases')
]