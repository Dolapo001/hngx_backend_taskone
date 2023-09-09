from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import datetime
import pytz

from .serializers import InfoSerializer
from .models import Info


class InfoView(APIView):
    @staticmethod
    def get(request):
        try:
            info = Info.objects.latest('id')
        except Info.DoesNotExist:
            info = None

        if info:
            serializer = InfoSerializer(info)
        else:
            slack_name = "adedolapo27"
            track = "Backend"
            github_file_url = "https://github.com/yourusername/yourrepo/blob/main/yourfile.py"
            github_source_code_url = "https://github.com/yourusername/yourrepo"
            current_time = datetime.datetime.now(pytz.utc)
            utc_offset = current_time.utcoffset().total_seconds() / 3600
            valid_utc = abs(utc_offset) <= 2

            data = {
                "slack_name": slack_name,
                "day_of_week": current_time.strftime('%A'),
                "current_utc_time": current_time.isoformat(),
                "utc_offset_valid": valid_utc,
                "track": track,
                "github_file_url": github_file_url,
                "github_source_code_url": github_source_code_url
            }

            serializer = InfoSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.data, status=status.HTTP_200_OK)
