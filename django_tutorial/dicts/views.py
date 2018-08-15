from rest_framework import viewsets
from rest_framework.decorators import action

from django_tutorial.dicts.models import Tag, Interest, Gender
from django_tutorial.accounts.permissions import IsAdminOrIsSelf, IsAdmin
from django_tutorial.dicts.serializers import TagSerializer, InterestSerializer, GenderSerializer


class TagViewSet(viewsets.ModelViewSet):
    """
    retrieve:
    Return the given tag.

    list:
    Return a list of all the existing tags.

    create:
    Create a new tag instance.

    delete:
    Delete the given tag.
    """
    permission_classes = (IsAdmin,)
    http_method_names = ['options', 'put', 'get', 'post', 'delete']

    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    @action(methods=['delete',], detail=False, permission_classes=[IsAdminOrIsSelf])
    def delete_tag(self, request, *args, **kwargs):
        print('deleted')


class InterestViewSet(viewsets.ModelViewSet):
    """
    retrieve:
    Return the given interest.

    list:
    Return a list of all the existing interests.

    create:
    Create a new interest instance.

    delete:
    Delete the given interest.
    """
    http_method_names = ['options', 'put', 'get', 'post', 'delete']
    permission_classes = (IsAdmin,)
    queryset = Interest.objects.all()
    serializer_class = InterestSerializer


class GenderViewSet(viewsets.ModelViewSet):
    """
    retrieve:
    Return the given gender.

    list:
    Return a list of all the existing genders.

    create:
    Create a new tag gender.

    delete:
    Delete the given gender.
    """
    http_method_names = ['options', 'put', 'get', 'post', 'delete']
    permission_classes = (IsAdmin,)
    queryset = Gender.objects.all()
    serializer_class = GenderSerializer
