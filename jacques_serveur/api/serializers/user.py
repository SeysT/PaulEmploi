from django.contrib.auth.models import User

from rest_framework import serializers

from api.models.user import Profile


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email')


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = (
            'user',
            'desired_min_salary',
            'desired_max_salary',
            'desired_location',
            'desired_contract',
            'interests',
            'degrees',
            'skills',
            'languages',
        )
