from django.db import models

class Metric(models.Model):
    datetime = models.DateTimeField()
    voltage = models.IntegerField()
    current = models.IntegerField()