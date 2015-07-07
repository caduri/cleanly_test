# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cleanly', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('product_header', models.CharField(max_length=20)),
                ('product_decription', models.CharField(max_length=200)),
                ('product_price', models.IntegerField()),
                ('artist', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
