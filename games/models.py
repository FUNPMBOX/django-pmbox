from django.db import models

class Stage(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return str(self.name)


class Phase(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return str(self.name)


class Material(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=1024)

    def __str__(self):
        return str(self.name)


class Game(models.Model):
    stage = models.ManyToManyField(Stage)
    phase = models.ManyToManyField(Phase)
    material = models.ManyToManyField(Material)
    duration = models.PositiveSmallIntegerField()
    max_people = models.PositiveSmallIntegerField()
    title = models.CharField(max_length=1024)
    description = models.TextField()
    short_description = models.TextField()
    image = models.FileField(null=True, blank=True)

    def __str__(self):
        return str(self.title)
