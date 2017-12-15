from django.db import models


class Degree(models.Model):
    name = models.CharField(max_length=255)


class Skill(models.Model):
    name = models.CharField(max_length=255)


class Language(models.Model):
    name = models.CharField(max_length=255)


class Contract(models.Model):
    name = models.CharField(max_length=255)


class Location(models.Model):
    name = models.CharField(max_length=255)
    gpsLatitude = models.BigIntegerField()
    gpsLongitude = models.BigIntegerField()


class Company(models.Model):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    description = models.CharField(max_length=255)


class Offer(models.Model):
    title = models.CharField(max_length=255)
    degree = models.ForeignKey(Degree, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    min_salary = models.BigIntegerField()
    max_salary = models.BigIntegerField()
    description = models.CharField(max_length=500)
    contract_type = models.ForeignKey(Contract, on_delete=models.CASCADE)
    weekly_work_time = models.BigIntegerField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    experience_name = models.CharField(max_length=255)
    creation_date = models.DateTimeField(auto_now_add=True)
