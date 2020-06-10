from django.urls import path
from .views import add_case , view_case , report_case, show_cases, advanced_search, search_cases, charge

urlpatterns = [
    path('new', add_case, name='add_case'),
    path('<int:id>', view_case, name='view_case'),
    path('<int:id>/report', report_case, name='report_case'),
    path('', show_cases, name='show_cases'),
    path('advanced_search', advanced_search, name='advanced_search'),
    path('search', search_cases, name='search_cases'),
    path('donation', charge, name='donation'),

]