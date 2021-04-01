from django.db import models


class App(models.Model):
    name = models.CharField(max_length=55)
    description = models.TextField()
