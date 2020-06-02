from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Vote, Donation, Report

# Register your models here.

admin.site.register(User,UserAdmin)
admin.site.register(Vote)
admin.site.register(Donation)
admin.site.register(Report)
