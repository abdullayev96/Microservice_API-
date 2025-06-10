from django.urls import path
from .views import *


urlpatterns = [
    path('question/', QuestionAPIView.as_view()),
    path('question/<int:pk>/', QuestionRetrieveAPIView.as_view())
]



