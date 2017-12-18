from django.contrib.auth.models import User
from api.models.user import Profile
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username')

class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(read_only=True, slug_field='username')

    class Meta:
        model = Profile
        fields = '__all__' # A modifier pour mettre les champs correspondant vraiment au profil utilisateur