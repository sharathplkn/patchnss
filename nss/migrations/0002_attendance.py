# Generated by Django 4.2.1 on 2024-01-21 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("nss", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Attendance",
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
                ("date", models.DateField()),
                ("roll_no", models.IntegerField()),
                ("department", models.CharField(max_length=20)),
            ],
        ),
    ]