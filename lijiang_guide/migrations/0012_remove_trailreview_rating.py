# Generated by Django 4.2.4 on 2023-08-22 09:50

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("lijiang_guide", "0011_rental"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="trailreview",
            name="rating",
        ),
    ]