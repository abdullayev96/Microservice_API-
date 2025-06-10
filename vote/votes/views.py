from rest_framework import generics
from .serializers import VoteSerializer
from .models import Vote
import requests
from django.http import HttpResponse
from django.http import JsonResponse



class VoteAPIView(generics.ListAPIView):
	queryset = Vote.objects.all()
	serializer_class = VoteSerializer




def test_question_service(request):
    try:
        response = requests.get("http://127.0.0.1:8002/api/question/2/")
        print("Status:", response.status_code)
        print("Response:", response.text)

        if response.status_code != 200:
            return JsonResponse({
                "error": f"API returned status code {response.status_code}",
                "response_text": response.text
            }, status=response.status_code)

        content_type = response.headers.get("Content-Type", "")
        if "application/json" not in content_type.lower():
            return JsonResponse({
                "error": f"Expected JSON, got Content-Type: {content_type}",
                "response_text": response.text
            }, status=400)

        if not response.text.strip():
            return JsonResponse({
                "error": "Empty response from API"
            }, status=400)

        try:
            data = response.json()
            return JsonResponse({
                "status_code": response.status_code,
                "data": data
            })
        except ValueError as json_error:
            return JsonResponse({
                "error": f"Invalid JSON: {str(json_error)}",
                "response_text": response.text
            }, status=400)

    except requests.exceptions.RequestException as e:
        print("Xatolik:", e)
        return JsonResponse({"error": f"Request failed: {str(e)}"}, status=500)
