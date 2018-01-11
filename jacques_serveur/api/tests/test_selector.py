from django.test import TestCase

from django.contrib.auth.models import User
from api.models.profile import Profile
from api.models.fields import Location, Contract, Interest, Degree, Skill
from api.models.offer import Offer, Company
from api.utils.selector import OfferSelector

from django.core.management import call_command

class OfferSelectorTest(TestCase):
    def setUp(self):
        self.user, created = User.objects.get_or_create(username='jean')

        self.user.profile.desired_location = Location.objects.create(
            city_name='PARIS 20, ILE-DE-FRANCE, FRANCE',
            gps_latitude=48,
            gps_longitude=2
        )
        self.user.profile.desired_contract=Contract.objects.create(name='Contrat à durée indéterminée')
        self.user.profile.desired_min_salary=500
        self.user.profile.desired_max_salary=10000
        self.user.save()

        self.companies = [
            Company.objects.create(name='Facebook'),
            Company.objects.create(name='Google')
        ]

        self.offers = [
            Offer.objects.create(
                title = 'Developpeur React',
                min_salary = 2500,
                max_salary = 3500,
                description = 'Un taff bien rigolo',
                contract_type = Contract.objects.get(name='Contrat à durée indéterminée'),
                weekly_work_time = '35h',
                company = Company.objects.create(name='Facebook'),
                location = Location.objects.get(city_name='PARIS 20, ILE-DE-FRANCE, FRANCE'),
            ),
            Offer.objects.create(
                title = 'Developpeur Python',
                min_salary = 3000,
                max_salary = 5000,
                description = 'Passion python needed',
                contract_type = Contract.objects.get(name='Contrat à durée indéterminée'),
                weekly_work_time = '35h',
                company = Company.objects.create(name='Google'),
                location =  Location.objects.create(
                    city_name='BORDEAUX, NOUVELLE-AQUITAINE, FRANCE',
                    gps_latitude=44,
                    gps_longitude=0
                )
            )
        ]

    def test_offer_selector_init(self):
        selector = OfferSelector(self.user.profile, self.offers)
        print("Selector", selector.get_interesting())
