from django.db import models

# Create your models here.

class CurrencyPair(models.Model):
    date = models.DateField()
    rand = models.FloatField()
    dollar = models.FloatField()
    australian_dollar = models.FloatField()

class CurrencyStory(models.Model):
    date = models.DateField()
    story = models.TextField()
