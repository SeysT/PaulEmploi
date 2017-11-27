from rest_framework import generics

from api.serializers.bucketlist_serializers import BucketlistSerializer
from api.models.bucketlist import Bucketlist


class BucketlistView(generics.ListCreateAPIView):
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer

    def perform_create(self, serializer):
        serializer.save()


class BucketlistDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer
