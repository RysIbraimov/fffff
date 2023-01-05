from rest_framework import serializers

from .models import Profile

class SenderProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['user',]
        read_only_fields = ['is_sender']

class BuyerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['user', ]
        read_only_fields = ['is_sender']



