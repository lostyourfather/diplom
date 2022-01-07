# Generated by Django 3.2.4 on 2022-01-04 01:31

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
            name='Work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('description', models.TextField(verbose_name='description')),
            ],
            options={
                'verbose_name': 'work',
                'verbose_name_plural': 'works',
            },
        ),
        migrations.CreateModel(
            name='WorkUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.IntegerField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('work_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_works.work')),
            ],
            options={
                'verbose_name': 'work for user',
                'verbose_name_plural': 'works for user',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='files/works-images/')),
                ('work_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_works.work')),
            ],
            options={
                'verbose_name': 'image',
                'verbose_name_plural': 'images',
            },
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('file', models.ImageField(blank=True, null=True, upload_to='files/works-files/')),
                ('work_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_works.work')),
            ],
            options={
                'verbose_name': 'file',
                'verbose_name_plural': 'files',
            },
        ),
    ]
