from django.urls import path
from .views import *


urlpatterns = [
    path('vote/', VoteAPIView.as_view()),
    path('request/<int:pk>/', test_question_service)
]