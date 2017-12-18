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
    language = serializers.SlugRelatedField(read_only=True, slug_field='name')
    location = serializers.SlugRelatedField(read_only=True, slug_field='name')
    degree = serializers.SlugRelatedField(read_only=True, slug_field='name')
    contract_type = serializers.SlugRelatedField(read_only=True, slug_field='name')

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


class OfferExpandSerializer(OfferSerializer):
    skill = serializers.SlugRelatedField(read_only=True, slug_field='name')
    company = CompanySerializer(read_only=True)
    location = LocationSerializer(read_only=True)

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
                  'creation_date',
                  'skill',
                  'description',
                  'weekly_work_time',
                  'experience_name')
