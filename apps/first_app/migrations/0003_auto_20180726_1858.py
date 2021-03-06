# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-07-26 18:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0002_group_contributions'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donation_has_cause',
            name='cause',
        ),
        migrations.RemoveField(
            model_name='donation_has_cause',
            name='donation',
        ),
        migrations.AddField(
            model_name='donation',
            name='amount',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='donation',
            name='cause',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='donation_has_causes', to='first_app.Cause'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='donation',
            name='groups',
            field=models.ManyToManyField(related_name='donations', to='first_app.Group'),
        ),
        migrations.DeleteModel(
            name='Donation_has_cause',
        ),
    ]
