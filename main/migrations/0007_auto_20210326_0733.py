# Generated by Django 3.1.6 on 2021-03-26 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20210326_0713'),
    ]

    operations = [
        migrations.AddField(
            model_name='beat_tasks',
            name='task_name',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='beat_tasks',
            name='task_type',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='division_tasks',
            name='task_name',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='division_tasks',
            name='task_type',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='range_tasks',
            name='task_name',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='range_tasks',
            name='task_type',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]