from django.db import models

# Create your models here.

class Building(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name    



class BuiltdingItem(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class BuildingSelectionList(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class BuildingSelectionListItem(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name