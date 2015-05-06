# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_auto_20150506_0927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promise',
            name='date_promised',
            field=models.DateField(null=True, verbose_name=b'Date', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='promise',
            name='fulfillment_proof',
            field=models.TextField(default='', null=True, verbose_name='Text', blank=True),
            preserve_default=True,
        ),
    ]
