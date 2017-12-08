from rest_framework import generics, permissions

from api.models.bucketlist import Bucketlist
from api.permissions import IsOwner
from api.serializers.bucketlist import BucketlistSerializer


class BucketlistView(generics.ListCreateAPIView):
    serializer_class = BucketlistSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Bucketlist.objects.filter(owner=self.request.user)


class BucketlistDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BucketlistSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner,)

    def get_queryset(self):
        return Bucketlist.objects.filter(owner=self.request.user)
