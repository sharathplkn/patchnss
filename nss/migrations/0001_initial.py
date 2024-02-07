# Generated by Django 4.2.1 on 2024-02-05 16:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Department",
            fields=[
                ("dep_id", models.IntegerField(primary_key=True, serialize=False)),
                ("dep_name", models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Event",
            fields=[
                ("event_id", models.AutoField(primary_key=True, serialize=False)),
                ("event_name", models.CharField(max_length=60)),
                ("date", models.DateField()),
                ("start_time", models.TimeField()),
                ("end_time", models.TimeField()),
                ("photo", models.ImageField(upload_to="events")),
                ("des", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Programme",
            fields=[
                (
                    "programme_id",
                    models.IntegerField(primary_key=True, serialize=False),
                ),
                ("program_name", models.CharField(max_length=65)),
                ("no_of_sems", models.IntegerField()),
                ("grad_level", models.CharField(max_length=10)),
                (
                    "dept_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="nss.department",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="volunteer",
            fields=[
                ("volunteer_id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=25)),
                ("guard_name", models.CharField(max_length=25)),
                ("guard_mob_no", models.IntegerField()),
                ("sex", models.CharField(max_length=15)),
                ("dob", models.DateField()),
                ("year", models.IntegerField()),
                ("community", models.CharField(max_length=15)),
                ("address", models.TextField()),
                ("blood_group", models.CharField(max_length=15)),
                ("height", models.IntegerField()),
                ("weight", models.IntegerField()),
                ("mobile_no", models.IntegerField()),
                ("Email_id", models.EmailField(max_length=254)),
                ("year_of_enrollment", models.IntegerField()),
                ("cultural_talents", models.TextField()),
                ("hobbies", models.TextField()),
                ("roll_no", models.IntegerField()),
                ("image", models.ImageField(default="", upload_to="volunteers")),
                (
                    "program_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="nss.programme",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Attendance",
            fields=[
                ("Attendance_id", models.AutoField(primary_key=True, serialize=False)),
                ("date", models.DateField()),
                ("roll_no", models.IntegerField(null=True)),
                ("name", models.CharField(max_length=30)),
                ("department", models.CharField(max_length=20)),
                (
                    "even_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="nss.event"
                    ),
                ),
                (
                    "vol_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="nss.volunteer"
                    ),
                ),
            ],
        ),
    ]
