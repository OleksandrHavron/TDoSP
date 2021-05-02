from django.db import models
from django.urls import reverse

import xml.etree.cElementTree as et


def is_svg(f):
    """
    Check if provided file is svg
    """
    f.seek(0)
    tag = None
    try:
        for event, el in et.iterparse(f, ('start',)):
            tag = el.tag
            break
    except et.ParseError:
        pass
    return tag == '{http://www.w3.org/2000/svg}svg'


class Category(models.Model):
    name = models.CharField(max_length=55)
    description = models.TextField()
    image = models.ImageField(upload_to='categories/images', blank=True)
    slug = models.SlugField(verbose_name='slug', max_length=50, unique=True)
    svg_icon = models.FileField(upload_to='categories/svg_icons', blank=True)

    class Meta:
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'

    def __str__(self):
        return self.name

    def get_all_subcategories(self):
        return SubCategory.objects.filter(category=self.pk)

    def get_svg_icon(self):
        with open(self.svg_icon.path) as svg_file:
            return svg_file.read()


class SubCategory(models.Model):
    name = models.CharField(max_length=55)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')
    description = models.TextField()
    image = models.ImageField(upload_to='subcategories/images/', blank=True)
    slug = models.SlugField(verbose_name='slug', max_length=50, unique=True)
    svg_icon = models.FileField(upload_to='subcategories/svg_icons', blank =True)

    class Meta:
        verbose_name = 'Підкатегорія'
        verbose_name_plural = 'Підкатегорії'

    def get_absolute_url(self):
        return reverse('app_list', kwargs={"subcategory_slug": self.slug})

    def get_all_apps(self):
        apps = App.objects.filter(subcategory=self.pk)
        return apps

    def get_svg_icon(self):
        with open(self.svg_icon.path) as svg_file:
            return svg_file.read()

    def __str__(self):
        return self.name


class App(models.Model):
    name = models.CharField('Назва', max_length=55)
    slug = models.SlugField(verbose_name='slug', max_length=50, unique=True)
    description = models.TextField('Опис')
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name='apps')
    file = models.FileField('Файл', upload_to='apps/files')
    image = models.ImageField('Лого', upload_to='apps/images', blank=True)
    update = models.DateTimeField(auto_now=True)
    developer = models.CharField('Розробник', max_length=55, blank=True)
    windows = models.CharField('Версія Windows', max_length=200, blank=True)
    language = models.CharField('Мова', max_length=200, blank=True)

    class Meta:
        verbose_name = 'Додаток'
        verbose_name_plural = 'Додаткі'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/app/{self.slug}'

    def get_props(self):
        return Prop.objects.filter(app=self)

    def get_images(self):
        return Image.objects.filter(app=self)


class Prop(models.Model):
    prop = models.TextField('Характеристика')
    app = models.ForeignKey(App, on_delete=models.CASCADE, related_name='props')
    
    class Meta:
        verbose_name = 'Характеристика'
        verbose_name_plural = 'Характеристики'


class Image(models.Model):
    image = models.ImageField('Зображення', upload_to='apps/images')
    app = models.ForeignKey(App, on_delete=models.CASCADE, related_name='images')

    class Meta:
        verbose_name = 'Зображення'
        verbose_name_plural = 'Зображення'
