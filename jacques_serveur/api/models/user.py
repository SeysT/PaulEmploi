from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from rest_framework.authtoken.models import Token

from api.models.offer import (
    Offer,
    Location,
    Interest,
    Degree,
    Skill,
    Language,
    Contract
)


class Profile(models.Model):
    """
    This class extends the User class from django using a OneToOne relation.
    + properties:
        - user: precise to relate to User model from Django
        - accepted_offers: all offers accepted by user
        - refused_offers: all offers refused by user
        - seen_offers: return all offers seen by user (combine accepted and refused offers)
        - offers_to_show: return all offers we might want to show to the user
    + methods:
        - accept_offer: add the given offer to accepted_offers
        - refuse_offer: add the given offer to refused_offers
        - _check_offer: raise exception if the given offer has been already seen
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    accepted_offers = models.ManyToManyField(Offer, related_name = 'accepted_by')
    refused_offers = models.ManyToManyField(Offer, related_name = 'refused_by')

    desired_location = models.ForeignKey(Location)
    interests = models.ManyToManyField(Interest)
    degrees = models.ManyToManyKey(Degree)
    skills = models.ManyToManyField(Skill)
    languages = models.ManyToManyField(Language)
    desired_min_salary = models.BigIntegerField()
    desired_max_salary = models.BigIntegerField()
    desired_contract = models.ForeignKey(Contract)

    @property
    def seen_offers(self):
        """Return all offers seen by the user"""
        return self.accepted_offers.all().union(self.refused_offers.all())

    @property
    def offers_to_show(self):
        """Return all offers we might want to show to the user"""
        return Offer.objects.difference(self.seen_offers.all())

    def accept_offer(self, offer):
        """This function wrapps the add function of accepted_offers attributes"""
        self._check_offer(offer)
        self.accepted_offers.add(offer)

    def refuse_offer(self, offer):
        """This function wrapps the add function of refused_offers attributes"""
        self._check_offer(offer)
        self.refused_offers.add(offer)

    def _check_offer(self, offer):
        """This function raise an exception if the given offer has already been seen by the user"""
        if offer in self.accepted_offers.all():
            raise AlreadyAcceptedOfferException
        elif offer in self.refused_offers.all():
            raise AlreadyRefusedOfferException


class AlreadySeenOfferException(Exception):
    """This exception can be raised when we detect the user has already seen a given offer."""
    def __init__(self, message='This offer has already been seen for this user.'):
        self.message = message

    def __str__(self):
        return self.message


class AlreadyAcceptedOfferException(AlreadySeenOfferException):
    """This exception can be raised when we detect the user has already accepted a given offer."""
    def __init__(self, message='This offer has already been accepted for this user.'):
        self.message = message


class AlreadyRefusedOfferException(AlreadySeenOfferException):
    """This exception can be raised when we detect the user has already refused a given offer."""
    def __init__(self, message='This offer has already been refused for this user.'):
        self.message = message


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """This function create a Profile every time a User is created"""
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """This function update the Profile model when the User model is saved"""
    instance.profile.save()


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
