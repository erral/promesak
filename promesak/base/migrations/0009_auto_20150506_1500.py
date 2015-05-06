# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_party_mayor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promise',
            name='source_promise_text',
            field=models.TextField(default='', null=True, verbose_name='Extra promise text', blank=True),
            preserve_default=True,
        ),
    ]
