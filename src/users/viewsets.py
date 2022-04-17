from django.contrib.auth.models import User

from rest_framework import viewsets, mixins

from .serializers import UserSerializer, ProfileSerializer

from .permissions import IsProfileOwnerOrReadOnly, IsUserOwnerOrGetAndPostOnly

from .models import Profile
from users import permissions, serializers


class UserViewSet(viewsets.ModelViewSet):
    permission_class = [IsUserOwnerOrGetAndPostOnly,]
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProfileViewSet(viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
    #mixins.ListModelMixin, mixins.CreatetModelMixin, mixins.DestroyModelMixin,
):
    permission_class = [IsProfileOwnerOrReadOnly,]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer