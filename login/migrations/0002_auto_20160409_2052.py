# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-09 20:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Song',
            new_name='Page',
        ),
    ]