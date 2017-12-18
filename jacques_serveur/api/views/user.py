from django.contrib.auth.models import User

from rest_framework import viewsets, status
from rest_framework.decorators import detail_route
from rest_framework.response import Response

from api.models.user import Profile
from api.serializers.offer import OfferSerializer
from api.serializers.user import UserSerializer, ProfileSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    @detail_route(methods=['get'])
    def profile(self, request, pk=None):
        if pk is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        try:
            user = User.objects.get(id=pk)
            profile = Profile.objects.get(user=user)
        except User.DoesNotExist or Profile.DoesNotExist:
            return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)

    @detail_route(methods=['get'])
    def accepted_offers(self, request, pk=None):
        if pk is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        try:
            user = User.objects.get(id=pk)
            profile = Profile.objects.get(user=user)
            accepted_offers = profile.accepted_offers
        except User.DoesNotExist or Profile.DoesNotExist:
            return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)
        serializer = OfferSerializer(accepted_offers, many=True)
        return Response(serializer.data)

    @detail_route(methods=['get'])
    def offers_to_show(self, request, pk=None):
        if pk is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        try:
            user = User.objects.get(id=pk)
            profile = Profile.objects.get(user=user)
            offers_to_show = profile.offers_to_show
        except User.DoesNotExist or Profile.DoesNotExist:
            return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)
        serializer = OfferSerializer(offers_to_show, many=True)
        return Response(serializer.data)

