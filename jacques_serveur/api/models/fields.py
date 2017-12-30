from django.db import models


class Degree(models.Model):
    name = models.CharField(max_length=255, null=True)


class Skill(models.Model):
    name = models.CharField(max_length=255, null=True)


class Interest(models.Model):
    name = models.CharField(max_length=255)


class Language(models.Model):
    name = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name


class Contract(models.Model):
    name = models.CharField(max_length=255, null=True)


class Location(models.Model):
    city_name = models.CharField(max_length=255)
    gps_latitude = models.BigIntegerField(null=True)
    gps_longitude = models.BigIntegerField(null=True)

    def __str__(self):
        return self.city_name