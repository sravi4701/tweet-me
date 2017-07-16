from django.contrib import admin

# Register your models here.

from tweets.models import Tweet

from .forms import TweetModelForm

# admin.site.register(Tweet)

class TweetModelAdmin(admin.ModelAdmin):
	form = TweetModelForm
	# class Meta:
	# 	model = Tweet
	# 	fields = [
	# 		'user',
	# 		'content'
	# 	]

admin.site.register(Tweet, TweetModelAdmin)

