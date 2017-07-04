from django.conf.urls import url

from .views import (tweet_detail_view, tweet_list_view)

urlpatterns = [
	url(r'^1/$', tweet_detail_view, name="detail"),
	url(r'^$', tweet_list_view, name="list"),

]