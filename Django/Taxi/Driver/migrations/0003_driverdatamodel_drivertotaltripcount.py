# Generated by Django 5.2 on 2025-05-04 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Driver', '0002_driverdatamodel_driverstatus'),
    ]

    operations = [
        migrations.AddField(
            model_name='driverdatamodel',
            name='DriverTotalTripCount',
            field=models.IntegerField(default=0, max_length=10),
        ),
    ]
