# Generated by Django 4.0.2 on 2022-02-22 12:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('africa', '0002_africamatchesfilter'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='africamatchesfilter',
            name='exclude_teams',
        ),
        migrations.RemoveField(
            model_name='africamatchesfilter',
            name='include_teams',
        ),
    ]
