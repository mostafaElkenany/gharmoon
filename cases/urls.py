from django.urls import path
from .views import add_case , view_case , report_case, show_cases, search, search_cases

urlpatterns = [
    path('new', add_case, name='add_case'),
    path('<int:id>', view_case, name='view_case'),
    path('<int:id>/report', report_case, name='report_case'),
    path('', show_cases, name='show_cases'),
    path('search', search, name='search'),
    path('results', search_cases, name='search_cases')
]