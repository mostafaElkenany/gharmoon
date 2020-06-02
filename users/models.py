from django.db import models
from  django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser
# from cases.models import Case

# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=40, unique=True)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.EmailField(('email address'), unique=True)
    mobile_phone = models.CharField(max_length=15,validators=[RegexValidator('^0(10|11|12|15)\d{8}$',message="please enter egyptian mobile phone: like= 01012345678")])
    profile_picture = models.ImageField(upload_to = 'images/', default='')
    case_reports = models.ManyToManyField('cases.Case',through='Report', related_name='reports', blank=True)
    case_votes = models.ManyToManyField('cases.Case', through='Vote', related_name='votes', blank=True)
    case_donations = models.ManyToManyField('cases.Case', through='Donation',related_name='donations', blank=True)
    signup_confirmation = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Vote(models.Model):
    user= models.ForeignKey('User', null=True, on_delete=models.CASCADE)
    case = models.ForeignKey('cases.Case', null=True, on_delete=models.CASCADE)
    vote = models.FloatField(null=True)

class Donation(models.Model):
    user= models.ForeignKey('User', null=True, on_delete=models.CASCADE)
    case = models.ForeignKey('cases.Case', null=True, on_delete=models.CASCADE)
    amount = models.FloatField(null=True)

class Report(models.Model):
    user= models.ForeignKey('User', null=True, on_delete=models.CASCADE)
    case = models.ForeignKey('cases.Case', null=True, on_delete=models.CASCADE)
   