from django.shortcuts import render
from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny

from .models import Profile
from .serializers import ProfileSenderSerializer,ProfileBuyerSerializer

class ProfileSenderViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSenderSerializer
    permission_classes = [AllowAny]

class ProfileBuyerViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileBuyerSerializer
    permission_classes = [AllowAny]
