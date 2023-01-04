from django.shortcuts import render
from rest_framework import generics

from .models import Profile
from .serializers import SenderProfileSerializer,BuyerProfileSerializer


class SenderRegisterApiView(generics.CreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = SenderProfileSerializer

class BuyerRegisterApiView(generics.CreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = BuyerProfileSerializer
