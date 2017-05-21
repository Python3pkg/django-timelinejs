# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-15 16:11


from django.db import migrations
import timelinejs.models


class Migration(migrations.Migration):

    dependencies = [
        ('timelinejs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='timeline',
            name='center_on',
            field=timelinejs.models.ListField(blank=True, help_text=b'Center the map on this location when loading. Give point coordinates, eg. [43.881, 3.324]'),
        ),
        migrations.AddField(
            model_name='timelineevent',
            name='location',
            field=timelinejs.models.ListField(blank=True, help_text=b'Project location. Give point coordinates, eg. [43.881, 3.324]'),
        ),
    ]
