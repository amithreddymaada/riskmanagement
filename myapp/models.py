from django.db import models

# Create your models here.

class CountriesInfo(models.Model):
    list_id = models.CharField(max_length=20)
    entity_key = models.CharField(max_length=2)


class RiskTable(models.Model):
    HighRisk = models.CharField(max_length=5000)
    MiddleRisk = models.CharField(max_length=5000)
    LowRisk = models.CharField(max_length=5000)