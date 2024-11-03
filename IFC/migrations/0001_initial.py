# Generated by Django 5.1.1 on 2024-11-03 08:11

import django.contrib.auth.models
import django.contrib.auth.validators
import django.utils.timezone
from django.db import migrations, models

import json


def create_chapter_models(apps, schema_editor):

    print("Creating chapter models...")

    # Get the model from the historical version
    Chapters = apps.get_model('IFC', 'Chapter')
    # Create predefined instances

    file = open('setup/init_chapter_data.json', 'r')
    data = json.load(file)

    for i in range(len(data)):
        ch = data[i]
        Chapters.objects.create(
            name=ch["name"],
            letters=ch["letters"],
            rush_chair=ch["rush_chair"],
            president=ch["president"],
            info=ch["info"],
            chapter_size=ch["chapter_size"],
            image=ch["image"]
        )

    file.close()


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('letters', models.CharField(max_length=10)),
                ('rush_chair', models.CharField(max_length=255)),
                ('president', models.CharField(max_length=255)),
                ('info', models.TextField(max_length=900)),
                ('chapter_size', models.PositiveIntegerField()),
                ('image', models.ImageField(default='chapters/default.jpg', upload_to='chapters/')),
            ],
        ),
        migrations.CreateModel(
            name='FSCUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all'
                  'permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'},
                  help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150,
                  unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()],
                  verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this'
                  'admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated'
                  'as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('affiliation', models.CharField(max_length=255)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get'
                  'all permissions granted to each of their groups.', related_name='user_set', related_query_name='user',
                  to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.',
                  related_name='user_set', related_query_name='user', to='auth.permission',
                  verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.RunPython(create_chapter_models)
    ]
