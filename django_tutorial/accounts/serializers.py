from django.contrib.auth.models import Group, User
from rest_framework import serializers

from django_tutorial.accounts.models import Profile
from django_tutorial.dicts.serializers import GenderSerializer, InterestSerializer


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(required=True)
    gender = GenderSerializer(required=False)
    interests = InterestSerializer(many=True, required=False)
    id = serializers.CharField(source='user.id')

    class Meta:
        model = Profile
        fields = ('id', 'user', 'age', 'gender', 'interests', )

    def create(self, validated_data):
        """
        Overriding the default create method of the Model serializer.
        :param validated_data: data containing all the details of student
        :return: returns a successfully created student record
        """
        user_data = validated_data.pop('user')
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        profile, created = Profile.objects.update_or_create(
            user=user,
            age=validated_data.pop('age'),
            gender=validated_data.pop('gender'),
            interests=validated_data.pop('interests')
        )
        return profile


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')
