from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import datetime
import pytz

from .serializers import InfoSerializer


class InfoView(APIView):
    @staticmethod
    def get(request):

        slack_name = "adedolapo27"

        current_day = datetime.datetime.now(pytz.utc).strftime('%A')

        current_time = datetime.datetime.now(pytz.utc)
        utc_offset = current_time.utcoffset().total_seconds() / 3600
        valid_utc = abs(utc_offset) <= 2

        track = "Backend"

        status_code = status.HTTP_200_OK

        file_url = "https://github.com/LoneStarrD/hngx_backend_taskone/blob/main/manage.py"

        source_code_url = "https://github.com/LoneStarrD/hngx_backend_taskone.git"

        data = {
            "SlackName": slack_name,
            "DayOfWeek": current_day,
            "CurrentUTCTime": current_time,
            "UTCOffsetValid": valid_utc,
            "Track": track,
            "GitHubFileURL": file_url,
            "GitHubSourceCodeURL": source_code_url,
            "StatusCode": status_code,
        }

        serializer = InfoSerializer(data)
        return Response(serializer.data, status=status.HTTP_200_OK)
