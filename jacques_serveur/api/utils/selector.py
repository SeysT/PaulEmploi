class Selector:

    def __init__(self, profile, available_objects):
        self.profile = profile
        self.available_objects = available_objects

    def compute_score(self, object):
        return 5

    def get_interesting(self, max_number=None):
        # Stocking interesting objects in an ordered list 'objects' where the
        # items of this list are tuples (object_id, score)
        objects = [
            (object.id, self.compute_score(object))
            for object in self.available_objects
            if self.compute_score(object) >= 5
        ]
        objects.sort(key=lambda object_tuple: object_tuple[1])
        ordered_objects_ids = [object[0] for object in objects][:max_number] if max_number != None \
            else [object[0] for object in objects]
        return ordered_objects_ids

class OfferSelector(Selector):

    def __init__(self, profile, available_offers):
        super().__init__(profile, available_offers)
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


class FormationSelector(Selector):

    def __init__(self, profile, available_formations):
        super().__init__(profile, available_formations)
        # definition of matching criteria
        self.desired_location = profile.desired_location
        self.skills = profile.skills
        self.languages = profile.languages
        self.interests = profile.interests
        self.degrees = profile.degrees

        # En fait il faudrait calculer combien d'offres supplémentaires cette formation ouvrirait ?


