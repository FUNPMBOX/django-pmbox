# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-12 18:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0008_auto_20180211_1816'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
