# Generated by Django 4.2.3 on 2023-07-20 14:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tasks", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Task",
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
                ("content", models.TextField()),
                ("datetime", models.DateTimeField(auto_now=True)),
                ("deadline", models.DateTimeField(blank=True, null=True)),
                ("done", models.BooleanField()),
                ("tag", models.ManyToManyField(related_name="tags", to="tasks.tag")),
            ],
        ),
    ]