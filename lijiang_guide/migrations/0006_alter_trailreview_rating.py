# Generated by Django 4.2.4 on 2023-08-06 04:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("lijiang_guide", "0005_trailreview"),
    ]

    operations = [
        migrations.AlterField(
            model_name="trailreview",
            name="rating",
            field=models.IntegerField(
                choices=[
                    (1, "One Star"),
                    (2, "Two Stars"),
                    (3, "Three Stars"),
                    (4, "Four Stars"),
                    (5, "Five Stars"),
                ],
                default=None,
            ),
        ),
    ]
