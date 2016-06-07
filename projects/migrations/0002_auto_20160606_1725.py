# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.text import slugify


def slug_fill(apps, _schema_editor):
    Project = apps.get_model("projects", "Project")
    for project in Project.objects.all():
        project.slug = slugify(project.name)
        project.save()

class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='slug',
            field=models.SlugField(default='', unique=True),
            preserve_default=False,
        ),
        migrations.RunPython(slug_fill),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(verbose_name='Name of the project', unique=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='project',
            name='number_of_users_required',
            field=models.PositiveSmallIntegerField(),
        ),
    ]
