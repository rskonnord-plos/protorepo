from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=256)

class Version(models.Model):
    item = models.ForeignKey(Item)
    hash_value = models.CharField(max_length=40)
