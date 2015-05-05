# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Party',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField(unique=True, max_length=255, verbose_name=b'Slug')),
                ('name', models.CharField(max_length=255, verbose_name='Title')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Promise',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField(unique=True, max_length=255, verbose_name=b'Slug')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('text', models.TextField(default='', verbose_name='Text')),
                ('date_promised', models.DateField(verbose_name=b'Start')),
                ('source_promise_url', models.CharField(max_length=255, verbose_name='Title')),
                ('source_promise_text', models.TextField(default='', verbose_name='Text')),
                ('party', models.ForeignKey(blank=True, to='base.Party', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
