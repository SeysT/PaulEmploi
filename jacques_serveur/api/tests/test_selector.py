from django.test import TestCase

from django.contrib.auth.models import User
from api.models.profile import Profile
from api.models.fields import Location, Contract, Interest, Degree, Skill, Language
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
        self.user.profile.desired_min_salary=1500
        self.user.profile.desired_max_salary=10000
        self.user.save()

        self.user.profile.skills.add(Skill.objects.create(name='CSS'))
        self.user.profile.skills.add(Skill.objects.create(name='HTML'))
        self.user.profile.skills.add(Skill.objects.create(name='Linux'))
        self.user.profile.degrees.add(Degree.objects.create(name='Informatique'))
        self.user.profile.languages.add(Language.objects.create(name='Francais'))

        # Ideal offer, should pass
        self.offer1 = Offer.objects.create(
            title = 'Developpeur React',
            min_salary = 2500,
            max_salary = 3500,
            description = 'Un taff bien rigolo',
            contract_type = Contract.objects.get(name='Contrat à durée indéterminée'),
            weekly_work_time = '35h',
            company = Company.objects.create(name='Facebook'),
            location = Location.objects.get(city_name='PARIS 20, ILE-DE-FRANCE, FRANCE'),
        )
        # ensures skill matching search
        self.offer1.skills.add(Skill.objects.create(name='css'))
        self.offer1.skills.add(Skill.objects.create(name='HTML5'))
        # no degree needed for that offer
        self.offer1.languages.add(Language.objects.get(name='Francais'))

        # Bad offer, should not pass
        self.offer2 = Offer.objects.create(
            title = 'Developpeur Python',
            min_salary = 1000,
            max_salary = 2000,
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
        self.offer2.skills.add(Skill.objects.create(name='Django'))
        self.offer2.skills.add(Skill.objects.create(name='Deep Learning'))
        self.offer2.degrees.add(Degree.objects.create(name='Informatique'))
        self.offer2.languages.add(Language.objects.create(name='Anglais'))

    def test_offer_selector(self):
        selector = OfferSelector(self.user.profile, [self.offer1, self.offer2])
        intereting_offers_ids = selector.get_interesting()
        self.assertTrue(self.offer1.id in intereting_offers_ids)
        self.assertFalse(self.offer2.id in intereting_offers_ids)