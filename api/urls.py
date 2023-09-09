from django.urls import path
from .views import InfoView

urlpatterns = [
    path('slack_name=adedolapo27&track=backend/', InfoView.as_view(), name='get_info'),
]
