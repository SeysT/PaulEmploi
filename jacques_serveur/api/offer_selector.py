from django.db import models
from api.models.offer import Offer, Location, Interest, Degree, Skill, Experience, Language, Contract
# from api.models.user import Profile


class Offer_Selector:


	def __init__(self, profile, avaiOff):
		self.availableOffers = avaiOff
		self.profile = profile
		self.interssOffers = None
		#definition of matching criteria
		self.desired_location = profile.desired_location
		self.desired_min_salary = profile.desired_min_salary
		self.desired_contract = profile.desired_contract
		self.skills = profile.skills
		self.language = profile.language

	def ComputeScore(self, offer):
		""" We select an offer if it's in the same city """
		score_location = 1 if offer.location.cityName == self.desired_location.cityName else 0
		""" We select an offer if it respect the min salary desired """
		score_minSalary = 1 if (offer.min_salary <= self.desired_min_salary or offer.min_salary == None) else 0
		""" We select an offer if it respect the kind of contracts desired """
		score_contract = 1 if(self.desired_contract in offer.contract_type) else 0
		""" languages are a +, count the number of languges satisfied """
		score_language = sum([1 if lang in self.language else 0 for lang in offer.language])
		"""count the number of skills satisfied
		exclude offers that dosn't contain skills, judged like not suitable for a person with skills :) """
		score_skills = sum([1 if skill in self.skills else 0 for skill in offer.skill]) 
		""" calculating the score, skills are weighted with 5, languages with 1 """
		score = score_location * score_minSalary * score_contract * (score_skills * 5 + score_language)
		return score

	def InterestingOffers(self, nombreMax):
		""" Stocking interesting offers in a ordered list 'temp' where the 
		elemets of this list are lists [offer, score]""" 
		temp = []
		for offer in self.availableOffers :
			score = self.ComputeScore(offer)
			""" an offer is selected if at least one skill is mastered by the user """
			if score >= 5:
				self.Insert_Offer(temp, offer, score)

		offer_ordered_pk = [liste[0].pk for liste in temp][:nombreMax]

		clauses = ' '.join(['WHEN id=%s THEN %s' % (pk, i) for i, pk in enumerate(offer_ordered_pk)])
		ordering = 'CASE %s END' % clauses
		self.interessentOffers = Offer.objects.filter(pk__in=pk_list).extra(
           select={'ordering': ordering}, order_by=('ordering',))
				
		return self.interessentOffers


	def Insert_Offer(list, offer, score):
		for i in range(len(list)):
			if score <= list[i][1]:
				list.insert(i, [offer,score])
				return

		list.append([offer, score])