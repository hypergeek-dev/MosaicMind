from rest_framework import serializers
from .models import Meeting

class MeetingSerializer(serializers.ModelSerializer):
    added_by_alias = serializers.SerializerMethodField()

    class Meta:
        model = Meeting
        fields = ['name', 'area', 'description', 'online_meeting_url', 'added_by_alias']

    def get_added_by_alias(self, obj):
        return obj.added_by.alias if obj.added_by else None
