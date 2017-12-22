from rest_framework import serializers

from api.models.offer import Degree, Skill, Language, Contract, Location, Company, Offer


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


class OfferIdSerializer(serializers.ModelSerializer):

    class Meta:
        model = Offer
        fields = ('id',)

class OfferSerializer(serializers.ModelSerializer):
    company = serializers.SlugRelatedField(read_only=True, slug_field='name')
    languages = LanguageSerializer(many=True, read_only=True)
    location = serializers.SlugRelatedField(read_only=True, slug_field='name')
    degrees = DegreeSerializer(many=True, read_only=True)
    contract_type = serializers.SlugRelatedField(read_only=True, slug_field='name')

    class Meta:
        model = Offer
        fields = ('title',
                'company',
                'languages',
                'location',
                'degrees',
                'min_salary',
                'max_salary',
                'contract_type',
                'creation_date')


class OfferExpandSerializer(OfferSerializer):
    skills = SkillSerializer(many=True, read_only=True)
    company = CompanySerializer(read_only=True)
    location = LocationSerializer(read_only=True)

    class Meta:
        model = Offer
        fields = ('title',
                  'company',
                  'languages',
                  'location',
                  'degrees',
                  'min_salary',
                  'max_salary',
                  'contract_type',
                  'creation_date',
                  'skills',
                  'description',
                  'weekly_work_time',
                  'experience_name')
