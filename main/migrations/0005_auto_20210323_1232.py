# Generated by Django 3.1.6 on 2021-03-23 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20210319_1113'),
    ]

    operations = [
        migrations.AddField(
            model_name='local_report',
            name='rtype',
            field=models.CharField(default='Demo', max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='report',
            name='rtype',
            field=models.CharField(default='Demo', max_length=1000),
            preserve_default=False,
        ),
    ]