# Generated by Django 4.1.3 on 2022-12-03 23:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("pets", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="pet",
            name="group",
        ),
    ]
