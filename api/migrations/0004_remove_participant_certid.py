# Generated by Django 2.2.5 on 2020-09-08 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20200908_2031'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='participant',
            name='certid',
        ),
    ]
