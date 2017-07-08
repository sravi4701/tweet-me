from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django import forms
from django.forms.utils import ErrorList
from .models import Tweet
from .forms import TweetModelForm
from .mixins import FormUserRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


class TweetDeleteView(DeleteView, LoginRequiredMixin):
	model = Tweet
	template_name = "tweets/delete_confirm.html"
	success_url = reverse_lazy("list")



class TweetUpdateView(LoginRequiredMixin, UpdateView):
	queryset = Tweet.objects.all()
	form_class = TweetModelForm
	template_name = "tweets/update_view.html"
	success_url = "/tweet/"


class TweetCreateView(LoginRequiredMixin, FormUserRequiredMixin, CreateView):
	form_class = TweetModelForm
	template_name = "tweets/create_view.html"
	success_url = "/tweet/create/"
	login_url = "/admin/"
	# def form_valid(self, form):
	# 	if self.request.user.is_authenticated():
	# 		form.instance.user = self.request.user
	# 		return super(TweetCreateView, self).form_valid(form)
	# 	else:
	# 		form.errors[forms.forms.NON_FIELD_ERRORS] = ErrorList(["User must be logged in to continue"])
	# 		return self.form_invalid(form)

class TweetListView(ListView):
	queryset = Tweet.objects.all()
	template_name = "tweets/list_view.html"
	def get_context_data(self, *args, **kwargs):
		context = super(TweetListView, self).get_context_data(*args, **kwargs)
		print(context)
		return context

class TweetDetailView(DetailView):
	template_name = "tweets/detail_view.html"
	queryset = Tweet.objects.all()

	def get_object(self):
		print(self.kwargs)
		pk = self.kwargs.get("pk")
		return get_object_or_404(Tweet,id=pk)

	def get_context_data(self, *args, **kwargs):
		context = super(TweetDetailView, self).get_context_data(*args, **kwargs)
		#print(context)
		return context


# def tweet_detail_view(request, id=1):
# 	obj = Tweet.objects.get(id=id)
# 	context = {'object': obj}
# 	return render(request, "tweets/detail_view.html", context)


# def tweet_list_view(request):
# 	obj = Tweet.objects.all()
# 	context = {'object':obj}
# 	return render(request, "tweets/list_view.html", context)