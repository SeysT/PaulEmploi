from rest_framework import viewsets, status
from rest_framework.decorators import list_route
from rest_framework.response import Response

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
            return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)
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
