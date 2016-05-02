# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0003_auto_20160323_1653'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nightlyrate',
            name='age_group',
        ),
        migrations.RemoveField(
            model_name='nightlyrate',
            name='house',
        ),
        migrations.DeleteModel(
            name='NightlyRate',
        ),
    ]
