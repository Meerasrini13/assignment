# Generated by Django 3.2 on 2022-09-12 00:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("corn", "add_timestamp_fields"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="corn",
            unique_together={("year",)},
        ),
    ]
