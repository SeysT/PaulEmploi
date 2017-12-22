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


class Company(models.Model):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255, null=True)
    description = models.CharField(max_length=1000, null=True)


class Formation(models.Model):
    name = models.CharField(max_length=255)
    required_skills = models.ManyToManyField(Skill, null=True)
    formation_skills = models.ManyToManyField(Skill, null=True)
    required_degree = models.ManyToManyField(Degree, null=True)
    formation_degree = models.ForeignKey(Degree, null=True)
    duree = models.CharField(max_length=255, null=True)


class Offer(models.Model):
    title = models.CharField(max_length=255)
    degrees = models.ManyToManyField(Degree)
    languages = models.ManyToManyField(Language)
    skills = models.ManyToManyField(Skill)
    min_salary = models.BigIntegerField(null=True)
    max_salary = models.BigIntegerField(null=True)
    description = models.CharField(max_length=5000, null=True)
    contract_type = models.ForeignKey(Contract, null=True)
    weekly_work_time = models.CharField(max_length=255, null=True)
    company = models.ForeignKey(Company, null=True)
    location = models.ForeignKey(Location, null=True)
    experience_name = models.CharField(max_length=255, null=True)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return """TITLE: {}\nDEGREE: {}\nLANGUAGE: {}\nSKILL: {}\n
        MIN_SALARY: {}\nMAX_SALARY: {}\nDESCRIPTION: {}\nCONTRACT_TYPE: {}\n
        WEEKLY_WORK_TIME: {}\nCOMPANY: {}\nLOCATION: {}\nSKILL: {}\n
        EXPERIENCE_NAME: {}\nCREATION_DATE: {}\n
        """.format(
            self.title,
            self.degrees,
            self.languages,
            self.skills,
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
