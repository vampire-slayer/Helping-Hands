# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-24 05:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Community',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('member', models.CharField(max_length=250)),
                ('logo', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('problem', models.CharField(max_length=250)),
                ('image', models.CharField(max_length=250)),
                ('community', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='community.Community')),
            ],
        ),
    ]
