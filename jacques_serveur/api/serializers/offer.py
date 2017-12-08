from rest_framework import serializers

from api.models.offer import Degree, Skill, Language, Contract, Location, Company, Offer

class OfferSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Offer
        fields = ('title',
                'company',
                'language',
                'min_salary',
                'max_salary',
                'contract_type',
                'creation_date')
