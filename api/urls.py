from django.urls import path
from .views import InfoView

urlpatterns = [
    path('get_info/', InfoView.as_view(), name='get_info'),
]
