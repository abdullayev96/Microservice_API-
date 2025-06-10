from django.urls import path
from .views import *



urlpatterns = [

    path('poll/', PollAPIView.as_view()),
    path('author/', AuthorAPI.as_view()),
]


