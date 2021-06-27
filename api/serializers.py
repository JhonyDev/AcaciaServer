from rest_framework import serializers

from admin_panel.models import ReportedAccounts
from .models import User, Photo, Interest, Expression


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
        model = Expression
        # fields = ('fixture_id', 'full_time_result')
        fields = '__all__'


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportedAccounts
        # fields = ('fixture_id', 'full_time_result')
        fields = '__all__'
