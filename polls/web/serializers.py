from rest_framework import serializers
from .models import Poll, Author



class PollSerializer(serializers.ModelSerializer):
	class Meta:
		model = Poll
		fields = ("vote", "category")


class AuthorSerializer(serializers.ModelSerializer):
	class Meta:
		model = Author
		fields = ('id', "full_name", "bio")
