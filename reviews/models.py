from django.db import models


class Publisher(models.Model):
    name = models.CharField(max_length=150, help_text='Nazwa wydawnictwa.')
    website = models.URLField(help_text='Witryna wydawnictwa.')
    email = models.EmailField(help_text='Adres email wydawnictwa.')