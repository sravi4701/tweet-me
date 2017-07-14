from django.conf.urls import url

from .views import (UserDetailView)

from django.views.generic import RedirectView

urlpatterns = [
	# url(r'^$', RedirectView.as_view(url="/")),
	# url(r'^$', TweetListAPIView.as_view(), name="list"), #api/tweet
	url(r'^(?P<username>[\w.@+-]+)/$', UserDetailView.as_view(), name="detail"),#profile/1
	# url(r'^create/$', TweetCreateAPIView.as_view(), name="create"), #tweet/create/
	# url(r'^(?P<pk>\d+)/edit$', TweetUpdateView.as_view(), name="edit"), #tweet/1/edit
	# url(r'^(?P<pk>\d+)/delete$', TweetDeleteView.as_view(), name="delete"), #tweet/1/delete
]