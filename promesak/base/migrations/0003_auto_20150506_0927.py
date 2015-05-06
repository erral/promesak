# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20150505_1013'),
    ]

    operations = [
        migrations.AddField(
            model_name='promise',
            name='fulfilled',
            field=models.BooleanField(default=False, verbose_name='Fulfilled?'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='promise',
            name='fulfillment_proof',
            field=models.TextField(default='', verbose_name='Text'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='promise',
            name='date_promised',
            field=models.DateField(verbose_name=b'Date'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='promise',
            name='source_promise_text',
            field=models.TextField(default='', verbose_name='Extra promise text'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='promise',
            name='source_promise_url',
            field=models.CharField(max_length=255, verbose_name='Source URL'),
            preserve_default=True,
        ),
    ]
