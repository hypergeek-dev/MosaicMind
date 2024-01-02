from rest_framework import serializers
from .models import Meeting
from django.contrib.auth.models import User

class MeetingSerializer(serializers.ModelSerializer):
    added_by_username = serializers.SerializerMethodField()

    class Meta:
        model = Meeting
        fields = [
            'meeting_id', 'name', 'meeting_time', 'approved', 'area',
            'description', 'online_meeting_url', 'added_by', 'added_by_username'
        ]
        extra_kwargs = {'added_by': {'read_only': True}}

    def get_added_by_username(self, obj):
        return obj.added_by.username if obj.added_by else None

    def create(self, validated_data):
        # Assuming 'request.user' is the currently logged-in user
        validated_data['added_by'] = self.context['request'].user
        return Meeting.objects.create(**validated_data)
