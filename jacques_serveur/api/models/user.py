from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from api.models.offer import Offer

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
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    accepted_offers = models.ManyToManyField(Offer, related_name='accepted_offers')
    refused_offers = models.ManyToManyField(Offer, related_name='refused_offers')

    @property
    def seen_offers(self):
        """Return all offers seen by the user"""
        return self.accepted_offers.all().union(self.refused_offers.all())

    @property
    def offers_to_show(self):
        """Return all offers we might want to show to the user"""
        return Offer.objects.difference(self.seen_offers.all())

    def accept_offer(self, offer):
        """This class wrapps the add function of accepted_offers attributes"""
        self.accepted_offers.add(offer)

    def refuse_offer(self, offer):
        """This class wrapps the add function of refused_offers attributes"""
        self.refused_offers.add(offer)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """This function create a Profile every time a User is created"""
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """This function update the Profile model when the User model is saved"""
    instance.profile.save()
