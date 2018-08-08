from rest_framework import serializers
from django_tutorial.dicts.models import Interest, Tag, Gender


class TagSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Tag
        fields = ('id', 'name', )


class GenderSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Gender
        fields = ('id', 'name', )


class InterestSerializer(serializers.HyperlinkedModelSerializer):
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Interest
        fields = ('id', 'name', 'tags')
