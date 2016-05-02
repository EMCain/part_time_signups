# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='camper',
            name='age_group',
            field=models.ForeignKey(default=1, to='signup.AgeGroup'),
        ),
        migrations.AddField(
            model_name='reservation',
            name='year',
            field=models.IntegerField(null=True),
        ),
    ]
