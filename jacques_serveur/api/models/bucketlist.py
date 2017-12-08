from django.db import models


class Bucketlist(models.Model):
    """This class represents the bucketlist model."""
    name = models.CharField(max_length=255, blank=False, unique=True)
    owner = models.ForeignKey(
        'auth.User',
        related_name='bucketlists',
        on_delete=models.CASCADE
    )
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)


    def __strt__(self):
        return "{}".format(self.name)

class Degree(models.Model) :
	name = models.CharField(max_length=255)

class Skills(models.Model) :
	name = models.CharField(max_length=255)

class Languages(models.Model) :
	name = models.CharField(max_length=255)

class Contracts(models.Model) :
	name = models.CharField(max_length=255)

class Locations(models.Model) :
	name = models.CharField(max_length=255)
	gpsLatitude = models.BigIntegerField()
	gpsLongitude = models.BigIntegerField()

class Offer(models.Model):
	title = models.CharField(max_length=255)
	degrees = models.CharField(max_length=255)
	languages = models.CharField(max_length=255)
	skills = models.CharField(max_length=255)
	minSalary = models.BigIntegerField()
	maxSalary = models.BigIntegerField()
	description = models.CharField(max_length=500)
	contractType = models.ForeignKey(Contracts, on_delete=models.CASCADE)
	weeklyWorkTime = models.BigIntegerField()
	companyName = models.CharField(max_length=255)
	companyUrl = models.CharField(max_length=255)
	companyDescription = models.CharField(max_length=255)
	location = models.ForeignKey(Locations, on_delete=models.CASCADE)
	experienceName = models.CharField(max_length=255)
	creationDate = models.DateTimeField(auto_now_add=True)