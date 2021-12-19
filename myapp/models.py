from django.db import models

# Create your models here.

class CountriesInfo(models.Model):
    list_id = models.CharField(max_length=20)
    entity_key = models.CharField(max_length=2)


