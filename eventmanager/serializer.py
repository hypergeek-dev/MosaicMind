from rest_framework import serializers
from .models import Meeting
from django.contrib.auth.models import User

class MeetingSerializer(serializers.ModelSerializer):
    added_by_username = serializers.SerializerMethodField()

    class Meta:
        model = Meeting
        fields = ['name', 'area', 'description', 'online_meeting_url', 'added_by_username']

    def get_added_by_username(self, obj):
        return obj.added_by.username if obj.added_by else None
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']  
