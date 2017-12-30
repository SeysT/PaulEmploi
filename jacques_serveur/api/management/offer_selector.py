from api.models import Offer


class OfferSelector:

    def __init__(self, profile, avai_offers):
        self.available_offers = avai_offers
        self.profile = profile
        # definition of matching criteria
        self.desired_location = profile.desired_location
        self.desired_min_salary = profile.desired_min_salary
        self.desired_contract = profile.desired_contract
        self.skills = profile.skills
        self.languages = profile.languages

    def compute_score(self, offer):
        # We select an offer if it's in the same city
        score_location = 1 if offer.location.city_name == self.desired_location.city_name else 0
        # We select an offer if it respects the min salary desired
        score_min_salary = 1 if (offer.min_salary <= self.desired_min_salary or offer.min_salary == None) else 0
        # We select an offer if it respects the kind of contract desired
        score_contract = 1 if self.desired_contract == offer.contract_type else 0
        # languages are a +, count the number of languages satisfied
        score_language = sum([1 if lang in self.languages else 0 for lang in offer.languages.all()])
        # count the number of skills satisfied
        # exclude offers that doesn't contain skills, judged like not suitable for a person with skills :)
        score_skills = sum([1 if skill in self.skills else 0 for skill in offer.skills.all()])
        # calculating the score, skills are weighted with 5, languages with 1
        score = score_location * score_min_salary * score_contract * (score_skills * 5 + score_language)
        return score

    def get_interesting_offers(self, max_number=None):
        # Stocking interesting offers in an ordered list 'offers' where the
        # elements of this list are tuples (offer_id, score)
        offers = [
            (offer.id, self.compute_score(offer))
            for offer in self.available_offers
            if self.compute_score(offer) >= 5
        ]
        offers.sort(key=lambda offer_tuple: offer_tuple[1])
        ordered_offers_ids = [offer[0] for offer in offers][:max_number] if max_number != None \
            else [offer[0] for offer in offers]
        return ordered_offers_ids

        # # Stocking interesting offers in a ordered list 'offers' where the
        # # elements of this list are tuples (offer, score)
        # offers = [
        #     (offer, self.compute_score(offer))
        #     for offer in self.available_offers
        #     if self.compute_score(offer) >= 5
        # ]
        # offers.sort(key=lambda offer_tuple: offer_tuple[1])
        # offer_ordered_pk = [liste[0].pk for liste in offers][:max_number] if max_number != None \
        #     else [liste[0].pk for liste in offers]
        #
        # # defining a query object that contains all the interesting offers sorted
        # clauses = ' '.join(['WHEN id=%s THEN %s' % (pk, i) for i, pk in enumerate(offer_ordered_pk)])
        # ordering = 'CASE %s END' % clauses
        # interesting_offers = Offer.objects.filter(pk__in=pk_list).extra(
        #     select={'ordering': ordering}, order_by=('ordering',))
        # return interesting_offers
