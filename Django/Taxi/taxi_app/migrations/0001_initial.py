# Generated by Django 5.2 on 2025-05-17 12:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Users', '0006_usersdatamodel_couponcode'),
    ]

    operations = [
        migrations.CreateModel(
            name='FinishReviewByCustomer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('statusCode', models.CharField(max_length=50)),
                ('customerReview', models.CharField(default='', max_length=5000)),
                ('rating', models.IntegerField()),
                ('date', models.DateField()),
                ('time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='ManagementModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('totalFairPrice', models.CharField(max_length=1000)),
                ('totalAmountTakenByUs', models.CharField(max_length=1000)),
                ('totalAmountShouldBeReturn', models.CharField(max_length=1000)),
                ('totalTripCount', models.CharField(max_length=30)),
                ('monthOfTotal', models.CharField(max_length=50)),
                ('yearOfTotal', models.CharField(max_length=5)),
                ('dateOfChecking', models.DateField()),
                ('timeOfChecking', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='PaymentManagement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('statusCode', models.CharField(max_length=50)),
                ('fairTaken', models.CharField(max_length=20)),
                ('dateOfFairTaken', models.DateField()),
                ('timeOfFairTaken', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='TaxiOnCancel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('statusCode', models.CharField(max_length=100)),
                ('DriverName', models.CharField(max_length=500)),
                ('CustomerName', models.CharField(max_length=500)),
                ('totalPassanger', models.CharField(max_length=10)),
                ('fairPrice', models.CharField(max_length=40)),
                ('taxiFrom', models.CharField(max_length=4000)),
                ('taxiTo', models.CharField(max_length=4000)),
                ('onCancelArea', models.CharField(max_length=4000)),
                ('review', models.CharField(max_length=5000)),
                ('cancelImage', models.ImageField(default='cancelReportImage/default/default.jpeg', upload_to='cancelReportImage/Report/')),
            ],
        ),
        migrations.CreateModel(
            name='TaxiOnFinish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('statusCode', models.CharField(max_length=50)),
                ('taxiDriver', models.CharField(max_length=500)),
                ('taxiCustomer', models.CharField(max_length=500)),
                ('totalPassanger', models.CharField(max_length=10)),
                ('taxiFrom', models.CharField(max_length=4000)),
                ('taxiTo', models.CharField(max_length=4000)),
                ('taxiStartTime', models.CharField(max_length=100)),
                ('taxiFinishTime', models.TimeField()),
                ('taxiDate', models.DateField()),
                ('fairPrice', models.CharField(max_length=40)),
                ('cuponCode', models.CharField(default='none', max_length=100)),
                ('fairTaxiPriceTaken', models.CharField(max_length=40)),
                ('driverReview', models.CharField(max_length=5000)),
                ('driverRating', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TaxiOnRunning',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('statusCode', models.CharField(max_length=50)),
                ('taxiDriverName', models.CharField(verbose_name=500)),
                ('taxiCustomerName', models.CharField(max_length=500)),
                ('totalPassanger', models.CharField(max_length=10)),
                ('taxiRunningFrom', models.CharField(max_length=4000)),
                ('taxiRunningTo', models.CharField(max_length=4000)),
                ('taxiStartTime', models.CharField(max_length=100)),
                ('taxiFutureEndTime', models.CharField(max_length=100)),
                ('taxiFairPrice', models.CharField(max_length=40)),
                ('cuponCode', models.CharField(default='none', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TaxiTimeOver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('toTaxiAvaId', models.CharField(max_length=50)),
                ('taxiCityAndLoc', models.CharField(max_length=2100)),
                ('avaPincode', models.CharField(default=' ', max_length=20)),
                ('dateAndTime', models.CharField(max_length=100)),
                ('toDate', models.DateField()),
                ('toTime', models.TimeField()),
                ('toDriverName', models.CharField(max_length=500)),
                ('toStatus', models.CharField(choices=[('Success', 'Success'), ('Failed', 'Failed')], default='Failed')),
            ],
        ),
        migrations.CreateModel(
            name='TaxiAvailable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taxiAvaId', models.CharField(max_length=50)),
                ('taxiCity', models.CharField(max_length=500)),
                ('currentLocation', models.CharField(max_length=2000)),
                ('pincode', models.CharField(default=' ', max_length=20)),
                ('taxiDate', models.DateField()),
                ('taxiTime', models.TimeField()),
                ('diverId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Users.usersdatamodel')),
            ],
        ),
    ]
