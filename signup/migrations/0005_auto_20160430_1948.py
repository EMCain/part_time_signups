# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0004_auto_20160430_1840'),
    ]

    operations = [
        migrations.CreateModel(
            name='HousingRateGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_camp_rate', models.BooleanField(default=True)),
                ('rate_1', models.DecimalField(default=0, max_digits=6, decimal_places=2)),
                ('rate_2', models.DecimalField(default=0, max_digits=6, decimal_places=2)),
                ('rate_3', models.DecimalField(default=0, max_digits=6, decimal_places=2)),
                ('rate_4', models.DecimalField(default=0, max_digits=6, decimal_places=2)),
                ('rate_5', models.DecimalField(default=0, max_digits=6, decimal_places=2)),
                ('rate_6', models.DecimalField(default=0, max_digits=6, decimal_places=2)),
                ('rate_7', models.DecimalField(default=0, max_digits=6, decimal_places=2)),
                ('age_group', models.ForeignKey(to='signup.AgeGroup')),
                ('hr_group', models.ForeignKey(to='signup.HousingRateGroup', null=True)),
            ],
        ),
        migrations.AddField(
            model_name='house',
            name='hr_group',
            field=models.ForeignKey(to='signup.HousingRateGroup', null=True),
        ),
    ]
