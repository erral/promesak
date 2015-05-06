# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_auto_20150506_1042'),
    ]

    operations = [
        migrations.AddField(
            model_name='party',
            name='mayor',
            field=models.CharField(default='', max_length=255, verbose_name='Mayor'),
            preserve_default=True,
        ),
    ]
