# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-14 09:05
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TimeRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datatime_records', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='TimeRecordLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('closed', models.BooleanField(default=False)),
                ('uuid', models.CharField(max_length=50)),
                ('datetimeIn', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='datetimein', to='timetable.TimeRecord')),
                ('datetimeout', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='datetimeout', to='timetable.TimeRecord')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='timelog', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
