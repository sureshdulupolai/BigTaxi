# Generated by Django 5.2 on 2025-05-23 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0010_reviewandrating'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviewandrating',
            name='userCategoryForRating',
            field=models.CharField(default='Customer', max_length=100),
        ),
    ]
