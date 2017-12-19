from django.db import models


class Degree(models.Model):
    name = models.CharField(max_length=255, null=True)


class Skill(models.Model):
    name = models.CharField(max_length=255, null=True)


class Language(models.Model):
    name = models.CharField(max_length=255, null=True)


class Contract(models.Model):
    name = models.CharField(max_length=255, null=True)


class Location(models.Model):
    name = models.CharField(max_length=255)
    gps_latitude = models.BigIntegerField(null=True)
    gps_longitude = models.BigIntegerField(null=True)


class Company(models.Model):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255, null=True)
    description = models.CharField(max_length=1000, null=True)


class Offer(models.Model):
    title = models.CharField(max_length=255)
    degree = models.ManyToManyField(Degree)
    language = models.ManyToManyField(Language)
    skill = models.ManyToManyField(Skill)
    min_salary = models.BigIntegerField(null=True)
    max_salary = models.BigIntegerField(null=True)
    description = models.CharField(max_length=5000, null=True)
    contract_type = models.ForeignKey(Contract, null=True)
    weekly_work_time = models.CharField(max_length=255, null=True)
    company = models.ManyToManyField(Company)
    location = models.ManyToManyField(Location)
    experience_name = models.CharField(max_length=255, null=True)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return """TITLE: {}\nDEGREE: {}\nLANGUAGE: {}\nSKILL: {}\n
        MIN_SALARY: {}\nMAX_SALARY: {}\nDESCRIPTION: {}\nCONTRACT_TYPE: {}\n
        WEEKLY_WORK_TIME: {}\nCOMPANY: {}\nLOCATION: {}\nSKILL: {}\n
        EXPERIENCE_NAME: {}\nCREATION_DATE: {}\n
        """.format(
            self.title,
            self.degree,
            self.language,
            self.skill,
            self.min_salary,
            self.max_salary,
            self.description,
            self.contract_type,
            self.weekly_work_time,
            self.company,
            self.location,
            self.experience_name,
            self.creation_date
        )
