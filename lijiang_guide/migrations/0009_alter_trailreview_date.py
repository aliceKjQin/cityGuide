# Generated by Django 4.2.4 on 2023-08-07 05:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("lijiang_guide", "0008_alter_trailreview_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="trailreview",
            name="date",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]