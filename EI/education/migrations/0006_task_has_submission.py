# Generated by Django 4.1.4 on 2023-03-12 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("education", "0005_task_filesubmission"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="has_submission",
            field=models.BooleanField(default=False),
        ),
    ]
