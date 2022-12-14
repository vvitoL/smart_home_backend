# Generated by Django 4.1.4 on 2022-12-13 07:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="device",
            name="amount_changes",
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="device",
            name="created",
            field=models.DateField(
                default=datetime.datetime(2022, 12, 13, 7, 47, 19, 262026)
            ),
        ),
        migrations.AddField(
            model_name="device",
            name="last_mod",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
