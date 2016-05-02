# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0005_auto_20160430_1948'),
    ]

    operations = [
        migrations.AddField(
            model_name='rate',
            name='year',
            field=models.IntegerField(default=0, max_length=4),
        ),
    ]
