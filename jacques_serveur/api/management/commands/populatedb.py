from django.core.management.base import BaseCommand
from api.models.offer import Offer


class Command(BaseCommand):
    help = 'Run this command to scrap the data from the Pole Emploi API and storing the result in the database'

    def handle(self, *args, **options):
        Offer.objects.create(
            title='test'
        )
