from django.contrib import admin

# Register your models here.

from tweets.models import Tweet

admin.site.register(Tweet)