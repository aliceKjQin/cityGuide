# Generated by Django 4.2.4 on 2023-08-07 06:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("lijiang_guide", "0009_alter_trailreview_date"),
    ]

    operations = [
        migrations.AddField(
            model_name="hiking",
            name="description",
            field=models.TextField(null=True),
        ),
    ]
