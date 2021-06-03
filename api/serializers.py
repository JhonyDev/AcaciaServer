from rest_framework import serializers

from .models import User, Photo, Interest, Liked


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = ('fixture_id', 'full_time_result')
        fields = '__all__'


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        # fields = ('fixture_id', 'full_time_result')
        fields = '__all__'


class InterestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interest
        # fields = ('fixture_id', 'full_time_result')
        fields = '__all__'


class LikedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Liked
        # fields = ('fixture_id', 'full_time_result')
        fields = '__all__'
