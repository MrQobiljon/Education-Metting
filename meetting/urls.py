from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('send_message/', send_message, name='send_message'),
    path('meetings/', meeting_list, name='meetings'),
    path('meeting/<int:pk>/', meeting_detail, name='meeting_detail'),
]