# Generated by Django 4.2.4 on 2023-08-06 04:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        (
            "lijiang_guide",
            "0004_remove_hiking_trail_image_hiking_hiking_image_and_more",
        ),
    ]

    operations = [
        migrations.CreateModel(
            name="TrailReview",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("review", models.TextField()),
                (
                    "rating",
                    models.IntegerField(
                        choices=[
                            ("one_star", "One Star"),
                            ("two_stars", "Two Stars"),
                            ("three_stars", "Three Stars"),
                            ("four_stars", "Four Stars"),
                            ("five_stars", "Five Stars"),
                        ],
                        default=None,
                    ),
                ),
                ("date", models.DateTimeField(auto_now_add=True)),
                (
                    "trail",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="lijiang_guide.hiking",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Trail Reviews",
            },
        ),
    ]
