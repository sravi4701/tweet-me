from django.db import models
from django.conf import settings
# Create your models here.
from tweets.validators import validate_content
from django.urls import reverse


class Tweet(models.Model):
	user 		= models.ForeignKey(settings.AUTH_USER_MODEL)
	content 	= models.CharField(max_length=140, validators=[validate_content])
	updated 	= models.DateTimeField(auto_now=True)
	timestamp 	= models.DateTimeField(auto_now_add=True)
	

	def __str__(self):
		return self.content

	def get_absolute_url(self, *args, **kwargs):
		return reverse("tweet:detail", kwargs={"pk":self.pk})
