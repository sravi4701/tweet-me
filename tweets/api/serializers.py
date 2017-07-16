from django.utils.timesince import timesince
from rest_framework import serializers

from tweets.models import Tweet

from accounts.api.serializers import UserDisplaySerializer

class TweetModelSerializer(serializers.ModelSerializer):
	user = UserDisplaySerializer(read_only=True)
	date_display = serializers.SerializerMethodField()
	timesince = serializers.SerializerMethodField()
	is_retweet = serializers.SerializerMethodField()
	class Meta:
		model = Tweet
		fields = [
			'user',
			'content',
			'timestamp',
			'date_display',
			'timesince',
			'id',
			'is_retweet',
		]

	def get_is_retweet(self, obj):
		if obj.parent:
			return True
		return False

	def get_date_display(self, obj):
		return obj.timestamp.strftime("%b %d, %Y %I:%M %p")

	def get_timesince(self, obj):
		return timesince(obj.timestamp ) + " ago"