# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-26 18:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='confirmed_member',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='member',
            name='joined',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]