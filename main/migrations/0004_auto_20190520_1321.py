# Generated by Django 2.1.4 on 2019-05-20 11:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20190514_1841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hand',
            name='hand_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 20, 13, 21, 46, 470412), verbose_name='date published'),
        ),
    ]
