from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import UserSerializer

from .permissions import IsUserOwnerOrGetAndPost


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [ IsUserOwnerOrGetAndPost ]
    serializer_class = UserSerializer
    queryset = User.objects.all()
