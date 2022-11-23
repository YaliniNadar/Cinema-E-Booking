# Generated by Django 4.1.3 on 2022-11-23 20:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [("core", "__first__")]

    operations = [
        migrations.CreateModel(
            name="Ticket",
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
                    "ticket_type",
                    models.CharField(
                        choices=[("AD", "ADULT"), ("CH", "CHILD"), ("SR", "SENIOR")],
                        max_length=2,
                    ),
                ),
                (
                    "showing",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.showing"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Booking",
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
                    "promo",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="core.promo",
                    ),
                ),
                (
                    "showing",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.showing"
                    ),
                ),
                ("tickets", models.ManyToManyField(to="checkout.ticket")),
            ],
        ),
    ]
