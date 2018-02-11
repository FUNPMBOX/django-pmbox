# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-11 14:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Phase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Stage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.RemoveField(
            model_name='game',
            name='people',
        ),
        migrations.AddField(
            model_name='game',
            name='max_people',
            field=models.PositiveSmallIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='game',
            name='phase',
            field=models.ManyToManyField(to='games.Phase'),
        ),
        migrations.AddField(
            model_name='game',
            name='stage',
            field=models.ManyToManyField(to='games.Stage'),
        ),
    ]