# Generated by Django 2.1.4 on 2019-05-14 16:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20190514_1712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hand',
            name='hand_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 14, 18, 41, 34, 785515), verbose_name='date published'),
        ),
    ]
