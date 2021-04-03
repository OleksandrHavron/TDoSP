from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=55)
    description = models.TextField()
    image = models.ImageField(upload_to='categories')

    class Meta:
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'

    def __str__(self):
        return self.name


class App(models.Model):
    name = models.CharField(max_length=55)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='apps')
    image = models.ImageField(upload_to='apps/')

    class Meta:
        verbose_name = 'Додаток'
        verbose_name_plural = 'Додаткі'

    def __str__(self):
        return self.name
