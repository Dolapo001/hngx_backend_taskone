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

        track = "Backend"

        status_code = status.HTTP_200_OK

        file_url = "https://github.com/LoneStarrD/hngx_backend_taskone/blob/main/manage.py"

        source_code_url = "https://github.com/LoneStarrD/hngx_backend_taskone.git"

        data = {
            "slack_name": slack_name,
            "current_day": current_day,
            "utc_time": current_time,
            "track": track,
            "github_file_url": file_url,
            "github_repo_url": source_code_url,
            "statuscode": status_code,
        }

        serializer = InfoSerializer(data)
        return Response(serializer.data, status=status.HTTP_200_OK)
