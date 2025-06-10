from rest_framework import generics
from .serializers import *
from .models import Poll, Author
from rest_framework.views import APIView, Response
from rest_framework import status



class PollAPIView(generics.ListCreateAPIView):
	queryset = Poll.objects.all()
	serializer_class = PollSerializer



class AuthorAPI(APIView):
	def get(self, request):
		try:
			authors = Author.objects.all()
			serializers = AuthorSerializer(authors, many=True)
			return Response({"data": serializers.data,
							 "status":status.HTTP_200_OK}, status=status.HTTP_200_OK)

		except Exception as e:
			print(e)

		return Response({"data": "Malumot topimadi !",
						 "status": status.HTTP_404_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND)