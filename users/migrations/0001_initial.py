# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django.contrib.auth.models
import django.core.validators
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, blank=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(help_text='Designates that this user has all permissions without explicitly assigning them.', default=False, verbose_name='superuser status')),
                ('username', models.CharField(max_length=30, help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', unique=True, verbose_name='username', error_messages={'unique': 'A user with that username already exists.'}, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')])),
                ('first_name', models.CharField(max_length=30, blank=True, verbose_name='first name')),
                ('last_name', models.CharField(max_length=30, blank=True, verbose_name='last name')),
                ('email', models.EmailField(max_length=254, blank=True, verbose_name='email address')),
                ('is_staff', models.BooleanField(help_text='Designates whether the user can log into this admin site.', default=False, verbose_name='staff status')),
                ('is_active', models.BooleanField(help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', default=True, verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('about_me', models.TextField(null=True, blank=True, verbose_name='about me')),
                ('avatar', models.ImageField(null=True, blank=True, upload_to='avatars')),
                ('my_project_experience', models.URLField(null=True, blank=True, verbose_name='URL for project')),
                ('phone', models.CharField(null=True, max_length=50, blank=True, verbose_name='phone')),
                ('groups', models.ManyToManyField(related_name='user_set', help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', verbose_name='groups', blank=True, to='auth.Group', related_query_name='user')),
                ('user_permissions', models.ManyToManyField(related_name='user_set', help_text='Specific permissions for this user.', verbose_name='user permissions', blank=True, to='auth.Permission', related_query_name='user')),
            ],
            options={
                'verbose_name_plural': 'users',
                'ordering': ['username'],
                'verbose_name': 'user',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('programming_lang', models.CharField(max_length=255, verbose_name='language')),
            ],
            options={
                'verbose_name_plural': 'skills',
                'verbose_name': 'skill',
            },
        ),
        migrations.CreateModel(
            name='SkillUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('level', models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(5)], verbose_name='level')),
                ('skill', models.ForeignKey(to='users.Skill')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'skills_users',
                'verbose_name': 'skill_user',
            },
        ),
        migrations.AddField(
            model_name='skill',
            name='skills',
            field=models.ManyToManyField(through='users.SkillUser', to=settings.AUTH_USER_MODEL),
        ),
    ]
