# Generated by Django 5.2 on 2025-05-23 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0012_rename_userstart_reviewandrating_userstar'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReviewBarcode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('barCode', models.CharField(max_length=1000)),
            ],
        ),
    ]
