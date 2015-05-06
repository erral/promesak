# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_auto_20150506_0943'),
    ]

    operations = [
        migrations.AddField(
            model_name='promise',
            name='date_fulfilled',
            field=models.DateField(null=True, verbose_name=b'Date fulfilled', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='promise',
            name='date_promised',
            field=models.DateField(null=True, verbose_name='Promise date', blank=True),
            preserve_default=True,
        ),
    ]
