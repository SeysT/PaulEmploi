import json

from rest_framework import viewsets, status
from rest_framework.decorators import list_route, detail_route
from rest_framework.response import Response

from api.models.offer import Contract, Location, Interest, Degree, Skill, Language
from api.models.user import Profile
from api.serializers.offer import OfferSerializer
from api.serializers.user import ProfileSerializer


class ProfileViewSet(viewsets.ViewSet):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

    def list(self, request):
        try:
            profile = request.user.profile
        except Profile.DoesNotExist:
            return Response({ 'detail': 'Not found.' }, status=status.HTTP_404_NOT_FOUND)
        return Response(self.serializer_class(profile).data)

    def put(self, request):
        try:
            profile = request.user.profile
            body = json.loads(request.body.decode())
        except Profile.DoesNotExist:
            return Response({ 'detail': 'Not found.' }, status=status.HTTP_404_NOT_FOUND)

        # for item in args.keys():
        #     try:
        #         setattr(profile, item, args[item])
        #     except ValueError or AttributeError:
        #         pass

        profile.desired_location = Location.objects.get(city_name=body['desired_location'])
        profile.desired_contract = Contract.objects.get(name=body['desired_contract'])

        for item in body['interests']:
            item = Interest.objects.get(name=item)
            profile.interests.add(item)
        for item in body['degrees']:
            item = Degree.objects.get(name=item)
            profile.degrees.add(item)
        for item in body['skills']:
            item = Skill.objects.get(name=item)
            profile.skills.add(item)
        for item in body['languages']:
            item = Language.objects.get(name=item)
            profile.languages.add(item)

        profile.desired_min_salary = body['desired_min_salary']
        profile.desired_max_salary = body['desired_max_salary']

        profile.save()
        return Response(self.serializer_class(profile).data)

    @list_route(methods=['get'])
    def accepted_offers(self, request):
        try:
            profile = request.user.profile
        except Profile.DoesNotExist:
            return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)
        accepted_offers = profile.accepted_offers
        serializer = OfferSerializer(accepted_offers, many=True)
        return Response(serializer.data)

    @list_route(methods=['get'])
    def offers_to_show(self, request):
        try:
            profile = request.user.profile
        except Profile.DoesNotExist:
            return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)
        offers_to_show = profile.offers_to_show
        serializer = OfferIdSerializer(offers_to_show, many=True)
        return Response(serializer.data)

