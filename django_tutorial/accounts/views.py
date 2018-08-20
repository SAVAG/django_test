from django.contrib.auth.models import User, Group
from rest_framework import viewsets

from django_tutorial.accounts.models import Profile
from django_tutorial.accounts.serializers import UserSerializer, GroupSerializer, ProfileSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class ProfileViewSet(viewsets.ModelViewSet):

    queryset = Profile.objects.filter(user__isnull=False).order_by('user__date_joined')
    serializer_class = ProfileSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
