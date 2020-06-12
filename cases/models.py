from django.db import models
from tinymce.models import HTMLField
from django.core.validators import MinValueValidator
from django.db.models.signals import pre_save
from datetime import datetime
from django.dispatch import receiver
from  django.core.validators import RegexValidator

# Create your models here.

class Case(models.Model) :
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    GOVERNRATES = ( 
        ('ALX', 'Alexandria'),
        ('ASN' ,'Aswan'), 
        ('AST', 'Asyut' ),
        ('BH' ,'Beheira' ),
        ('BNS', 'Beni Suef'), 
        ('C', 'Cairo' ),
        ('DK', 'Dakahlia'), 
        ('DT', 'Damietta' ),
        ('FYM', 'Faiyum' ),
        ('GH', 'Gharbia' ),
        ('GZ', 'Giza' ),
        ('IS', 'Ismailia'), 
        ('KFS', 'Kafr El Sheikh'), 
        ('LX', 'Luxor' ),
        ('MT', 'Matruh' ),
        ('MN', 'Minya' ),
        ('MNF', 'Monufia'), 
        ('WAD', 'New Valley'), 
        ('SIN', 'North Sinai'), 
        ('PTS', 'Port Said'),
        ('KB','Qalyubia'),
        ('KN', 'Qena'),
        ('BA', 'Red Sea'), 
        ('SHR', 'Sharqia'), 
        ('SHG', 'Sohag'),
        ('JS', 'South Sinai'), 
        ('SUZ', 'Suez'),
    )
    name = models.CharField(max_length=70, null=True)
    national_id = models.CharField(
        max_length=14,
        validators=[
            RegexValidator('^(2|3)[0-9][1-9][0-1][1-9][0-3][1-9](01|02|03|04|11|12|13|14|15|16|17|18|19|21|22|23|24|25|26|27|28|29|31|32|33|34|35|88)\d\d\d\d\d$',
        message="please enter a valid egyptian national ID"
        )],
        null=True
        )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    age = models.IntegerField(null=True, validators = [MinValueValidator(18)])
    jail_name = models.CharField(max_length=70,null=True)
    governerate = models.CharField(max_length=3,choices=GOVERNRATES,null=True)
    convection_date = models.DateField(null= True, blank=True)
    jail_time = models.IntegerField(null=True, validators = [MinValueValidator(1)])
    no_of_dependents = models.IntegerField(null=True, validators = [MinValueValidator(0)])
    total_target = models.FloatField(null=True, validators = [MinValueValidator(0.1)])
    details = HTMLField(null=True)
    owner = models.ForeignKey('users.User', null=True, on_delete=models.CASCADE)
    is_approved= models.BooleanField(null=True,blank=True)
    is_featured= models.BooleanField(null=True,blank=True)
    featuring_date= models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return self.name

#a trigger to auto update featuring date when the project is featured
@receiver(pre_save, sender=Case)
def update_case_on_save(sender, instance, **kwargs):
    if instance.id:
        old_case = Case.objects.get(pk=instance.id)
        if instance.is_featured and not old_case.is_featured:
            instance.featuring_date= datetime.now()