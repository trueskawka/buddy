# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(verbose_name='Name of the project', max_length=255)),
                ('description', models.TextField()),
                ('expiration_date', models.DateField()),
                ('number_of_users_required', models.IntegerField()),
                ('opensource', models.BooleanField()),
                ('url', models.URLField()),
                ('skills', models.ManyToManyField(to='users.Skill')),
                ('users', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
