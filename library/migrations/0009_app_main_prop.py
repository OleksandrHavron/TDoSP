# Generated by Django 3.1.7 on 2021-05-01 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0008_auto_20210430_1957'),
    ]

    operations = [
        migrations.AddField(
            model_name='app',
            name='main_prop',
            field=models.TextField(blank=True),
        ),
    ]