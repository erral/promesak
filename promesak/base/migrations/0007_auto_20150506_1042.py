# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_auto_20150506_0944'),
    ]

    operations = [
        migrations.AddField(
            model_name='party',
            name='candidates',
            field=models.TextField(default='', verbose_name='Candidates'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='party',
            name='logo',
            field=models.ImageField(upload_to=b'uploads', null=True, verbose_name='Logo', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='party',
            name='program_file',
            field=models.FileField(upload_to=b'uploads', null=True, verbose_name='Program file', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='party',
            name='text',
            field=models.TextField(default='', verbose_name='Text'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='party',
            name='web',
            field=models.CharField(default='', max_length=255, verbose_name='Web'),
            preserve_default=True,
        ),
    ]
