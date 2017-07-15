from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.views.generic import DetailView
from django.contrib.auth import get_user_model
from django.views import View
from accounts.models import UserProfile

User = get_user_model()

class UserDetailView(DetailView):

	template_name = "accounts/user_profile.html"

	def get_queryset(self):
		return User.objects.all()

	def get_object(self, *args, **kwargs):
		return get_object_or_404(User, username__iexact=self.kwargs.get("username"))

	def get_context_data(self, *args, **kwargs):
		context = super(UserDetailView, self).get_context_data(*args, **kwargs)
		following = UserProfile.objects.is_following(self.request.user, self.get_object())
		context["following"] = following
		return context

class UserFollowView(View):
	def get(self, request, username, *args, **kwargs):
		toggle_user = get_object_or_404(User, username__iexact=username)
		if request.user.is_authenticated():
			# user_profile, created = UserProfile.objects.get_or_create(user=request.user)
			is_following = UserProfile.objects.toggle_follow(self.request.user, toggle_user)

		return redirect("account:detail", username=username)

		# url = reverse("account:detail")
		# HttpResponseRedirect(url)

# user_profile = self.request.user.profile