# Generated by Django 4.2.4 on 2023-10-06 11:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='node',
            old_name='display_home',
            new_name='display_name',
        ),
    ]
