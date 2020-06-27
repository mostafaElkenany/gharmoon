from django.contrib import admin
from .models import Case
# Register your models here.
class CaseAdmin(admin.ModelAdmin):
    list_display = ('name','featuring_date','is_approved','is_completed')
    list_filter = ('is_featured','is_approved','is_completed')


admin.site.register(Case,CaseAdmin)
