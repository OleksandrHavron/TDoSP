# Generated by Django 3.1.7 on 2021-04-07 06:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_auto_20210407_0921'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='description',
        ),
    ]
