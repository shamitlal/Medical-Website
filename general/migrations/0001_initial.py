# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-10 11:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=25000)),
                ('heading', models.TextField(default=b' ')),
                ('key', models.TextField(default=b' ')),
            ],
        ),
    ]