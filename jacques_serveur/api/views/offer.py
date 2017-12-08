from rest_framework import generics, permissions

from api.models.offer import Offer
from api.permissions import IsOwner
from api.serializers.offer import OfferSerializer


class OfferView(generics.ListAPIView):
    serializer_class = OfferSerializer
    # permission_classes = (permissions.IsAuthenticated, IsOwner,)

    def get_queryset(self):
        return Offer.objects.all()

class OfferDetailView(generics.RetrieveAPIView):
    serializer_class = OfferSerializer

    def get_queryset(self):
        return Offer.objects.all()