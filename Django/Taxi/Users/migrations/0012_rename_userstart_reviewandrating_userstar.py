# Generated by Django 5.2 on 2025-05-23 17:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0011_reviewandrating_usercategoryforrating'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reviewandrating',
            old_name='userStart',
            new_name='userStar',
        ),
    ]
