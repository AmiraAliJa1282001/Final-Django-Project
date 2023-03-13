# Generated by Django 4.1.4 on 2023-03-13 10:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("education", "0007_alter_filesubmission_student"),
        ("landingPage", "0004_contactmessages"),
    ]

    operations = [
        migrations.CreateModel(
            name="Blacklist",
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
                ("teacher_rating", models.IntegerField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="education.student",
                    ),
                ),
            ],
        ),
    ]