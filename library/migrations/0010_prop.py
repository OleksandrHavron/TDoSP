# Generated by Django 3.1.7 on 2021-05-01 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0009_app_main_prop'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prop', models.TextField()),
                ('app', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='props', to='library.app')),
            ],
        ),
    ]
