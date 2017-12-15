from rest_framework import generics, permissions

from api.models.offer import Offer, Degree, Language, Skill, Contract, Location, Company
from api.permissions import IsOwner
from api.serializers.offer import OfferSerializer, OfferExpandSerializer, DegreeSerializer, LanguageSerializer, SkillSerializer, ContractSerializer, LocationSerializer, CompanySerializer


class OfferView(generics.ListAPIView):
    serializer_class = OfferSerializer
    # permission_classes = (permissions.IsAuthenticated, IsOwner,)

    def get_queryset(self):
        return Offer.objects.all()

class OfferDetailView(generics.RetrieveAPIView):
    serializer_class = OfferSerializer

    def get_queryset(self):
        return Offer.objects.all()

class OfferExpandView(generics.RetrieveAPIView):
    serializer_class = OfferExpandSerializer

    def get_queryset(self):
        return Offer.objects.all()

# class DegreeDetailView(generics.RetrieveAPIView):
#     serializer_class = DegreeSerializer
#
#     def get_queryset(self):
#         return Degree.objects.all()
#
# class LanguageDetailView(generics.RetrieveAPIView):
#     serializer_class = LanguageSerializer
#
#     def get_queryset(self):
#         return Language.objects.all()
#
# class SkillDetailView(generics.RetrieveAPIView):
#     serializer_class = SkillSerializer
#
#     def get_queryset(self):
#         return Skill.objects.all()
#
# class ContractDetailView(generics.RetrieveAPIView):
#     serializer_class = ContractSerializer
#
#     def get_queryset(self):
#         return Contract.objects.all()
#
# class LocationDetailView(generics.RetrieveAPIView):
#     serializer_class = LocationSerializer
#
#     def get_queryset(self):
#         return Location.objects.all()
#
# class CompanyDetailView(generics.RetrieveAPIView):
#     serializer_class = CompanySerializer
#
#     def get_queryset(self):
#         return Company.objects.all()
