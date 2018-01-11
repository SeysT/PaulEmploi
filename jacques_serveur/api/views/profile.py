import json

from rest_framework import viewsets, status
from rest_framework.decorators import list_route
from rest_framework.response import Response

from api.models.fields import Contract, Location, Interest, Degree, Skill, Language
from api.models.profile import Profile
from api.serializers.formation import FormationIdSerializer
from api.serializers.offer import OfferIdSerializer
from api.serializers.profile import ProfileSerializer


class ProfileViewSet(viewsets.ViewSet):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

    # GET '/api/profile/'
    def list(self, request):
        try:
            profile = request.user.profile
        except Profile.DoesNotExist:
            return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)
        return Response(self.serializer_class(profile).data)

    # PUT '/api/profile/'
    def put(self, request):
        try:
            profile = request.user.profile
            body = json.loads(request.body.decode())
        except Profile.DoesNotExist:
            return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)

        # for item in args.keys():
        #     try:
        #         setattr(profile, item, args[item])
        #     except ValueError or AttributeError:
        #         pass

        profile.desired_location = Location.objects.get(city_name=body['desired_location'])
        profile.desired_contract = Contract.objects.get(name=body['desired_contract'])

        profile.interests = Interest.objects.none()
        for item in body['interests']:
            item = Interest.objects.get(name=item)
            profile.interests.add(item)
        profile.degrees = Degree.objects.none()
        for item in body['degrees']:
            item = Degree.objects.get(name=item)
            profile.degrees.add(item)
        profile.skills = Skill.objects.none()
        for item in body['skills']:
            item = Skill.objects.get(name=item)
            profile.skills.add(item)
        profile.languages = Language.objects.none()
        for item in body['languages']:
            item = Language.objects.get(name=item)
            profile.languages.add(item)

        profile.desired_min_salary = body['desired_min_salary']
        profile.desired_max_salary = body['desired_max_salary']

        profile.save()
        return Response(self.serializer_class(profile).data)

    # GET '/api/profile/accepted_offers/'
    @list_route(methods=['get'])
    def accepted_offers(self, request):
        try:
            profile = request.user.profile
        except Profile.DoesNotExist:
            return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)
        accepted_offers = profile.accepted_offers
        serializer = OfferIdSerializer(accepted_offers, many=True)
        return Response(serializer.data)

    # GET '/api/profile/offers_to_show/'
    @list_route(methods=['get'])
    def offers_to_show(self, request):
        try:
            profile = request.user.profile
        except Profile.DoesNotExist:
            return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)
        offers_to_show = profile.offers_to_show
        return Response(offers_to_show)

    # GET '/api/profile/kept_formations/'
    @list_route(methods=['get'])
    def kept_formations(self, request):
        try:
            profile = request.user.profile
        except Profile.DoesNotExist:
            return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)
        kept_formations = profile.kept_formations
        serializer = FormationIdSerializer(kept_formations, many=True)
        return Response(serializer.data)

    # GET '/api/profile/formations_to_show/'
    @list_route(methods=['get'])
    def formations_to_show(self, request):
        try:
            profile = request.user.profile
        except Profile.DoesNotExist:
            return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)
        formations_to_show = profile.formations_to_show
        return Response(formations_to_show)
