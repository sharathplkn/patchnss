# Generated by Django 4.2.1 on 2024-02-05 16:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("nss", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="programme",
            old_name="dept_id",
            new_name="dept",
        ),
        migrations.RenameField(
            model_name="volunteer",
            old_name="program_id",
            new_name="program",
        ),
    ]