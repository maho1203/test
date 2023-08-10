# Generated by Django 4.2.3 on 2023-07-27 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="item",
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
                ("code", models.IntegerField()),
                ("name", models.TextField()),
                ("price", models.IntegerField()),
            ],
        ),
    ]