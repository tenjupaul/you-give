# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-07-26 21:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0003_auto_20180726_1858'),
    ]

    operations = [
        migrations.AddField(
            model_name='cause',
            name='logo_img',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='profile_pic',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]
