from django.urls import path
from .views import add_case , view_case , report_case

urlpatterns = [
    path('new', add_case, name='add_case'),
    path('<int:id>', view_case, name='view_case'),
    path('<int:id>/report', report_case, name='report_case'),
]