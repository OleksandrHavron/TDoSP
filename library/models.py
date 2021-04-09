from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=55)
    description = models.TextField()
    image = models.ImageField(upload_to='categories', blank=True)
    slug = models.SlugField(verbose_name='slug', max_length=50, unique=True, blank=False)

    class Meta:
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'

    def __str__(self):
        return self.name

    def get_all_subcategories(self):
        return SubCategory.objects.filter(category=self.pk)


class SubCategory(models.Model):
    name = models.CharField(max_length=55)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')
    description = models.TextField()
    image = models.ImageField(upload_to='apps/', blank=True)
    slug = models.SlugField(verbose_name='slug', max_length=50, unique=True, blank=False)

    class Meta:
        verbose_name = 'Підкатегорія'
        verbose_name_plural = 'Підкатегорії'

    def get_absolute_url(self):
        return reverse('app_list', kwargs={"subcategory_slug": self.slug})

    def get_all_apps(self):
        apps = App.objects.filter(subcategory=self.pk)
        return apps

    def __str__(self):
        return self.name


class App(models.Model):
    name = models.CharField(max_length=55)
    description = models.TextField()
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name='apps')
    file = models.FileField(upload_to='apps/files', default=None, blank=True)
    image = models.ImageField(upload_to='apps/images', blank=True)
    slug = models.SlugField(verbose_name='slug', max_length=50, unique=True, blank=False)

    class Meta:
        verbose_name = 'Додаток'
        verbose_name_plural = 'Додаткі'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/app/{self.slug}'
