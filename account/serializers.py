from rest_framework import serializers

from .models import Profile

class SenderProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['user',]

    def create(self, validated_data):
        new_sender = Profile(
            user = validated_data['user'],
            is_sender = True
        )
        new_sender.save()
        return new_sender


class BuyerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['user', ]

    def create(self, validated_data):
        new_sender = Profile(
            user=validated_data['user'],
            is_sender=False
        )
        new_sender.save()
        return new_sender


