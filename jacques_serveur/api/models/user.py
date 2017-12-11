from django.db import models
from api.models.bucketlist import Offer

class User(models.Model):
	firstName = models.CharField(max_length=255, blank=False)
	lastName = models.CharField(max_length=255, blank=False)
	mail = models.EmailField(max_length=255, blank=False, unique= True)
	age = models.BigIntegerField()
	formations = models.CharField()
	experiences = models.CharField()
	hobbies = models.CharField(max_length=255)


class AcceptedOffer(models.Model):
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	id = models.ForeignKey(Offer, on_delete = models.CASCADE)

class RefusedOffer(models.Model):
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	id = models.ForeignKey(Offer, on_delete = models.CASCADE)

