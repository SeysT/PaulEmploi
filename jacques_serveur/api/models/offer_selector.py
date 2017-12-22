from django.db import models

from api.models.offer import Offer, Location, Interest, Degree, Skill, Experience, Language, Contract


class Offer_Selector:

    def __init__(self, profile, avaiOff):
        self.available_offers = avaiOff
        self.profile = profile
        # definition of matching criteria
        self.desired_location = profile.desired_location
        self.desired_min_salary = profile.desired_min_salary
        self.desired_contract = profile.desired_contract
        self.skills = profile.skills
        self.languages = profile.language

    def compute_score(self, offer):
        # We select an offer if it's in the same city
        score_location = 1 if offer.location.cityName == self.desired_location.cityName else 0
        # We select an offer if it respect the min salary desired
        score_min_salary = 1 if (offer.min_salary <= self.desired_min_salary or offer.min_salary == None) else 0
        # We select an offer if it respect the kind of contracts desired
        score_contract = 1 if(self.desired_contract in offer.contract_type) else 0
        # languages are a +, count the number of languges satisfied
        score_language = sum([1 if lang in self.languages else 0 for lang in offer.language])
        # count the number of skills satisfied
        # exclude offers that dosn't contain skills, judged like not suitable for a person with skills :) 
        score_skills = sum([1 if skill in self.skills else 0 for skill in offer.skills]) 
        # calculating the score, skills are weighted with 5, languages with 1
        score = score_location * score_min_salary * score_contract * (score_skills * 5 + score_language)
        return score

    def get_interesting_offers(self, nombreMax):
        # Stocking interesting offers in a ordered list 'temp' where the 
        # elemets of this list are lists [offer, score]
        offers = [
            (offer, self.compute_score(offer))
            for offer in self.available_offers
            if self.compute_score(offer) >= 5
        ]
        offers.sort(key=lambda offer_tuple: offer_tuple[1])
        offer_ordered_pk = [liste[0].pk for liste in offers][:nombreMax]
        # definning a query object that contains all the interessting offers sorted
        clauses = ' '.join(['WHEN id=%s THEN %s' % (pk, i) for i, pk in enumerate(offer_ordered_pk)])
        ordering = 'CASE %s END' % clauses
        interesting_offers = Offer.objects.filter(pk__in=pk_list).extra(
           select={'ordering': ordering}, order_by=('ordering',))
        return interesting_offers