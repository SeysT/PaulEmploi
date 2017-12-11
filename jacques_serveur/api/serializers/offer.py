from rest_framework import serializers

from api.models.offer import Degree, Skill, Language, Contract, Location, Company, Offer

class OfferSerializer(serializers.ModelSerializer):

    class Meta:
        model = Offer
        fields = ('title',
                'company',
                'language',
                'location',
                'degree',
                'min_salary',
                'max_salary',
                'contract_type',
                'creation_date')

class OfferExpandSerializer(serializers.ModelSerializer):

    class Meta:
        model = Offer
        fields = ('skill',
                  'description',
                  'weekly_work_time',
                  'experience_name')

class DegreeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Degree
        fields = '__all__'


class LanguageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Language
        fields = '__all__'

class SkillSerializer(serializers.ModelSerializer):

    class Meta:
        model = Skill
        fields = '__all__'

class ContractSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contract
        fields = '__all__'

class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = '__all__'

class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = '__all__'
