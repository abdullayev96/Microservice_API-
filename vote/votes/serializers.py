from rest_framework import serializers
from .models import Vote
import requests


class VoteSerializer(serializers.ModelSerializer):
    question_data = serializers.SerializerMethodField()

    class Meta:
        model = Vote
        fields = ('id', 'question_id', 'question_data', 'date_updated')

    def get_question_data(self, obj):
        try:
            response = requests.get(f'http://127.0.0.1:8002/api/question/{obj.question_id}/')
            print(response.json(), "hello")
            if response.status_code == 200:
                return response.json()
        except Exception:
            return {"error": "Question service unreachable"}
        return None

