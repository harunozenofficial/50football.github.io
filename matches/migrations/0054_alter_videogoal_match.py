# Generated by Django 4.1.2 on 2022-10-12 14:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("matches", "0053_delete_matchtweet"),
    ]

    operations = [
        migrations.AlterField(
            model_name="videogoal",
            name="match",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="videos",
                to="matches.match",
            ),
        ),
    ]