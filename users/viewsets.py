from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import UserSerializer, ProfileSerializer
from .models import Profile

from .permissions import IsUserOwnerOrGetAndPost, IsProfileOwnerOrReadOnly
from rest_framework import viewsets, mixins


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [ IsUserOwnerOrGetAndPost ]
    serializer_class = UserSerializer
    queryset = User.objects.all()

# class ProfileViewSet(viewsets.ModelViewSet):
#     permission_classes = [ IsProfileOwnerOrReadOnly ]
#     serializer_class = ProfileSerializer
#     queryset = Profile.objects.all()

'''
    Perfroming generic viewsets and mixens
'''

class ProfileViewSet(viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.UpdateModelMixin):
    permission_classes = [ IsProfileOwnerOrReadOnly ]
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
