# Generated by Django 5.0.7 on 2024-07-29 11:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='biografi',
            new_name='bio',
        ),
    ]
