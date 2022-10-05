# Generated by Django 4.1 on 2022-10-05 06:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("core", "0008_movie_cast_alter_promo_code_alter_promo_exp_date")]

    operations = [
        migrations.RemoveField(model_name="movie", name="cast"),
        migrations.AlterField(
            model_name="promo",
            name="code",
            field=models.CharField(default="KE4HUD", max_length=6),
        ),
        migrations.AlterField(
            model_name="promo",
            name="exp_date",
            field=models.DateField(
                default=datetime.datetime(2022, 11, 4, 2, 11, 2, 230052)
            ),
        ),
    ]
