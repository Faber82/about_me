# Generated by Django 2.2.6 on 2019-11-17 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reps', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='image',
            field=models.FilePathField(default=False, path='static/img'),
        ),
        migrations.AddField(
            model_name='link',
            name='technology',
            field=models.TextField(default=False),
        ),
        migrations.AlterField(
            model_name='link',
            name='description',
            field=models.TextField(default=False),
        ),
    ]