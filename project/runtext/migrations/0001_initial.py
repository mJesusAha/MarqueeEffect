# Generated by Django 5.0.4 on 2024-04-10 20:34

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Runtext",
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
                ("text", models.CharField(max_length=254)),
                ("color", models.CharField(max_length=254)),
                ("background", models.CharField(max_length=254)),
            ],
        ),
    ]
