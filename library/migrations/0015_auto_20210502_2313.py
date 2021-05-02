# Generated by Django 3.1.7 on 2021-05-02 20:13

from django.db import migrations, models
import library.models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0014_merge_20210502_2258'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'verbose_name': 'Зображення', 'verbose_name_plural': 'Зображення'},
        ),
        migrations.AlterModelOptions(
            name='prop',
            options={'verbose_name': 'Характеристика', 'verbose_name_plural': 'Характеристики'},
        ),
        migrations.AlterField(
            model_name='app',
            name='description',
            field=models.TextField(verbose_name='Опис'),
        ),
        migrations.AlterField(
            model_name='app',
            name='developer',
            field=models.CharField(blank=True, max_length=55, verbose_name='Розробник'),
        ),
        migrations.AlterField(
            model_name='app',
            name='file',
            field=models.FileField(upload_to='apps/files', verbose_name='Файл'),
        ),
        migrations.AlterField(
            model_name='app',
            name='image',
            field=models.ImageField(blank=True, upload_to='apps/images', verbose_name='Лого'),
        ),
        migrations.AlterField(
            model_name='app',
            name='language',
            field=models.CharField(blank=True, max_length=200, verbose_name='Мова'),
        ),
        migrations.AlterField(
            model_name='app',
            name='name',
            field=models.CharField(max_length=55, verbose_name='Назва'),
        ),
        migrations.AlterField(
            model_name='app',
            name='windows',
            field=models.CharField(blank=True, max_length=200, verbose_name='Версія Windows'),
        ),
        migrations.AlterField(
            model_name='category',
            name='svg_icon',
            field=models.FileField(blank=True, upload_to='categories/svg_icons', validators=[library.models.validate_svg]),
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='apps/images', verbose_name='Зображення'),
        ),
        migrations.AlterField(
            model_name='prop',
            name='prop',
            field=models.TextField(verbose_name='Характеристика'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='svg_icon',
            field=models.FileField(blank=True, upload_to='subcategories/svg_icons', validators=[library.models.validate_svg]),
        ),
    ]