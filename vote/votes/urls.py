from django.urls import path
from .views import *


urlpatterns = [
    path('vote/', VoteAPIView.as_view()),
    path('request', test_question_service)
]