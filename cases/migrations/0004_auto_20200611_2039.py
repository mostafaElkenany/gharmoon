# Generated by Django 3.0.6 on 2020-06-11 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0003_auto_20200607_2053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='governerate',
            field=models.CharField(choices=[('ALX', 'Alexandria'), ('ASN', 'Aswan'), ('AST', 'Asyut'), ('BH', 'Beheira'), ('BNS', 'Beni Suef'), ('C', 'Cairo'), ('DK', 'Dakahlia'), ('DT', 'Damietta'), ('FYM', 'Faiyum'), ('GH', 'Gharbia'), ('GZ', 'Giza'), ('IS', 'Ismailia'), ('KFS', 'Kafr El Sheikh'), ('LX', 'Luxor'), ('MT', 'Matruh'), ('MN', 'Minya'), ('MNF', 'Monufia'), ('WAD', 'New Valley'), ('SIN', 'North Sinai'), ('PTS', 'Port Said'), ('KB', 'Qalyubia'), ('KN', 'Qena'), ('BA', 'Red Sea'), ('SHR', 'Sharqia'), ('SHG', 'Sohag'), ('JS', 'South Sinai'), ('SUZ', 'Suez')], max_length=3, null=True),
        ),
    ]
