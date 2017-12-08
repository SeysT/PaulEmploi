from rest_framework.permissions import BasePermission

from api.models.bucketlist import Bucketlist


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if isinstance(obj, Bucketlist):
            return obj.owner == request.user
        return obj.owner == request.user
