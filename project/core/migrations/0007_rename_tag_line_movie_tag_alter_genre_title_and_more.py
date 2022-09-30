# Generated by Django 4.1 on 2022-09-28 23:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("core", "0006_genre_alter_promo_exp_date_movie_genres")]

    operations = [
        migrations.RenameField(model_name="movie", old_name="tag_line", new_name="tag"),
        migrations.AlterField(
            model_name="genre",
            name="title",
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name="movie",
            name="runtime",
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="promo",
            name="code",
            field=models.CharField(default="2M4G1Y", max_length=6),
        ),
        migrations.AlterField(
            model_name="promo",
            name="exp_date",
            field=models.DateField(
                default=datetime.datetime(2022, 10, 28, 19, 49, 47, 297579)
            ),
        ),
    ]
