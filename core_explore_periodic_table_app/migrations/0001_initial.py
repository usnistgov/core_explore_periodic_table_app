""" Migrations
"""

# Generated by Django 3.2.10 on 2021-12-29 20:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    """Migration"""

    initial = True

    dependencies = [
        ("core_main_app", "0001_initial"),
        ("core_explore_keyword_app", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ExplorePeriodicTable",
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
            ],
            options={
                "verbose_name": "core_explore_periodic_table_app",
                "permissions": (
                    (
                        "access_explore_periodic_table",
                        "Can access explore periodic table",
                    ),
                ),
                "default_permissions": (),
            },
        ),
        migrations.CreateModel(
            name="SearchOperatorMapping",
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
                (
                    "search_operator",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="core_explore_keyword_app.searchoperator",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PersistentQueryPeriodicTable",
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
                ("user_id", models.CharField(max_length=200)),
                ("content", models.TextField(blank=True, null=True)),
                ("data_sources", models.JSONField(blank=True, default=list)),
                ("creation_date", models.DateTimeField(auto_now_add=True)),
                (
                    "name",
                    models.CharField(
                        blank=True, max_length=200, null=True, unique=True
                    ),
                ),
                (
                    "templates",
                    models.ManyToManyField(
                        blank=True, default=[], to="core_main_app.Template"
                    ),
                ),
            ],
            options={
                "abstract": False,
                "verbose_name": "Persistent Query by Periodic Table",
                "verbose_name_plural": "Persistent Queries by Periodic Table",
            },
        ),
    ]