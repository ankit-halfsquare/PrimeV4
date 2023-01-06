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


class Project(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class ProjectSelectionList(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class ProjectSelectionListItem(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class SkillsLevel(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class People(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name




