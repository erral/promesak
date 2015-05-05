# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='party',
            name='slug',
            field=models.SlugField(null=True, max_length=255, blank=True, unique=True, verbose_name=b'Slug'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='promise',
            name='slug',
            field=models.SlugField(null=True, max_length=255, blank=True, unique=True, verbose_name=b'Slug'),
            preserve_default=True,
        ),
    ]
