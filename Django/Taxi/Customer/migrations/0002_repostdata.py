# Generated by Django 5.2 on 2025-05-31 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='repostData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PNRCode', models.CharField(max_length=100)),
                ('userCode', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('driverCode', models.CharField(max_length=100)),
                ('text', models.CharField(max_length=5000)),
                ('date', models.DateField(auto_now_add=True)),
                ('time', models.TimeField(auto_now_add=True)),
            ],
        ),
    ]
