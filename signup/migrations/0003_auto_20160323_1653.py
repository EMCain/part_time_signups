# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0002_auto_20160323_1637'),
    ]

    operations = [
        migrations.AddField(
            model_name='nightlyrate',
            name='base_rate',
            field=models.DecimalField(default=0, max_digits=6, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='nightlyrate',
            name='nightly_rate',
            field=models.DecimalField(default=0, max_digits=6, decimal_places=2),
        ),
    ]
