from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Tweet
from django.urls import reverse

User = get_user_model()

class TweetModelTestCase(TestCase):

	def setUp(self):
		some_random_user = User.objects.create(username="ravi33333333333")

	def test_tweet_item(self):
		obj = Tweet.objects.create(
				user=User.objects.first(),
				content="Some random content"
			)

		self.assertTrue(obj.content == "Some random content")
		self.assertTrue(obj.id == 1)

		absolute_url = reverse("tweet:detail", kwargs={"pk":1})

		self.assertTrue(obj.get_absolute_url(), absolute_url)