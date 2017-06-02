# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-06 22:38
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('flows', '0079_reset_1'),
        ('channels', '0051_reset_2'),
    ]

    operations = [
        migrations.AddField(
            model_name='channelsession',
            name='flow',
            field=models.ForeignKey(help_text='The flow this session was part of', null=True, on_delete=django.db.models.deletion.CASCADE, to='flows.Flow'),
        ),
        migrations.AddField(
            model_name='channelsession',
            name='modified_by',
            field=models.ForeignKey(help_text='The user which last modified this item', on_delete=django.db.models.deletion.CASCADE, related_name='channels_channelsession_modifications', to=settings.AUTH_USER_MODEL),
        ),
    ]
