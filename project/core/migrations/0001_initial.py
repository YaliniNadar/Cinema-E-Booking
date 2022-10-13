# Generated by Django 4.1 on 2022-10-13 05:35

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [migrations.swappable_dependency(settings.AUTH_USER_MODEL)]

    operations = [
        migrations.CreateModel(
            name="Genre",
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
                ("title", models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Movie",
            fields=[
                (
                    "id",
                    models.IntegerField(primary_key=True, serialize=False, unique=True),
                ),
                ("title", models.CharField(max_length=200)),
                ("tag", models.TextField(blank=True, null=True)),
                ("rating", models.CharField(max_length=200)),
                ("runtime", models.CharField(max_length=200, null=True)),
                ("release_date", models.DateField(null=True)),
                ("synopsis", models.TextField(blank=True, null=True)),
                ("pic", models.ImageField(blank=True, null=True, upload_to="images/")),
                ("trailer_url", models.URLField(blank=True, null=True)),
                ("producer", models.CharField(blank=True, max_length=200, null=True)),
                ("director", models.CharField(blank=True, max_length=200, null=True)),
                ("actor_ids", models.CharField(max_length=200, null=True)),
                ("genres", models.ManyToManyField(to="core.genre")),
            ],
            options={"verbose_name_plural": "Movies"},
        ),
        migrations.CreateModel(
            name="MPAA",
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
                ("rating", models.CharField(max_length=200, unique=True)),
            ],
            options={"verbose_name_plural": "MPAA Rating"},
        ),
        migrations.CreateModel(
            name="Promo",
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
                ("name", models.CharField(max_length=200)),
                ("code", models.CharField(default="7UQ1UN", max_length=6)),
                (
                    "discount",
                    models.DecimalField(decimal_places=2, default=0.1, max_digits=3),
                ),
                (
                    "exp_date",
                    models.DateField(
                        default=datetime.datetime(2022, 11, 12, 1, 35, 5, 107105)
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Showing",
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
                ("showtime", models.DateTimeField()),
                ("room", models.CharField(max_length=200)),
                (
                    "movie",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.movie"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Profile",
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
                ("receive_promos", models.BooleanField()),
                (
                    "user",
                    models.OneToOneField(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
