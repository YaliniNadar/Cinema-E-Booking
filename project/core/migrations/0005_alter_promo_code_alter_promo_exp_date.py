# Generated by Django 4.1 on 2022-10-13 06:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("core", "0004_alter_promo_code_alter_promo_exp_date")]

    operations = [
        migrations.AlterField(
            model_name="promo",
            name="code",
            field=models.CharField(default="0EHDRC", max_length=6),
        ),
        migrations.AlterField(
            model_name="promo",
            name="exp_date",
            field=models.DateField(
                default=datetime.datetime(2022, 11, 12, 2, 13, 26, 690851)
            ),
        ),
    ]
