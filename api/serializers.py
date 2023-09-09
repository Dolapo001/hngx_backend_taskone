from rest_framework import serializers

class InfoSerializer(serializers.Serializer):
    SlackName = serializers.CharField()
    DayOfWeek = serializers.CharField()
    CurrentUTCTime = serializers.DateTimeField()
    UTCOffsetValid = serializers.BooleanField()
    Track = serializers.CharField()
    GitHubFileURL = serializers.URLField()
    GitHubSourceCodeURL = serializers.URLField()
    StatusCode = serializers.CharField()
