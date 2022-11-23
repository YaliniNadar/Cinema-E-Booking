# Generated by Django 4.1.3 on 2022-11-23 20:22

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Actor",
            fields=[
                (
                    "id",
                    models.IntegerField(primary_key=True, serialize=False, unique=True),
                ),
                ("name", models.CharField(max_length=200)),
                ("pic", models.ImageField(default="", upload_to="actors/")),
            ],
        ),
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
            name="PhysicalSeat",
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
                ("seat_row", models.CharField(max_length=1)),
                ("seat_number", models.IntegerField()),
            ],
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
                ("code", models.CharField(default="3THVAP", max_length=6)),
                (
                    "discount",
                    models.DecimalField(decimal_places=2, default=0.1, max_digits=3),
                ),
                (
                    "exp_date",
                    models.DateField(
                        default=datetime.datetime(2022, 12, 23, 15, 22, 57, 964659)
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SeatInShowing",
            fields=[
                (
                    "physical_seat",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to="core.physicalseat",
                    ),
                ),
                ("reserved", models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name="ShowRoom",
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
                ("seats", models.ManyToManyField(null=True, to="core.physicalseat")),
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
                ("tag", models.TextField()),
                (
                    "runtime",
                    models.CharField(help_text="in mins", max_length=200, null=True),
                ),
                ("release_date", models.DateField(null=True)),
                ("synopsis", models.TextField(default="")),
                ("pic", models.ImageField(default="", upload_to="images/")),
                ("trailer_url", models.URLField(default="www.youtube.com")),
                ("producer", models.CharField(max_length=200, null=True)),
                ("director", models.CharField(default="", max_length=200)),
                (
                    "actor_ids",
                    models.ManyToManyField(to="core.actor", verbose_name="Actors"),
                ),
                ("genres", models.ManyToManyField(to="core.genre")),
                (
                    "rating",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.mpaa"
                    ),
                ),
            ],
            options={"verbose_name_plural": "Movies"},
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
                (
                    "movie",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.movie"
                    ),
                ),
                (
                    "room",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.showroom"
                    ),
                ),
            ],
            options={"unique_together": {("showtime", "room")}},
        ),
    ]
