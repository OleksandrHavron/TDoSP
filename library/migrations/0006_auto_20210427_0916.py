# Generated by Django 3.1.7 on 2021-04-27 06:16

from django.db import migrations, models
import library.models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0005_auto_20210427_0903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='svg_icon',
            field=models.FileField(blank=True, upload_to='categories/svg_icons'),
        ),
    ]
