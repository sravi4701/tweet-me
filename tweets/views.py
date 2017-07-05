from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Tweet



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
		return Tweet.objects.get(id=1)

	def get_context_data(self, *args, **kwargs):
		context = super(TweetDetailView, self).get_context_data(*args, **kwargs)
		print(context)
		return context


# def tweet_detail_view(request, id=1):
# 	obj = Tweet.objects.get(id=id)
# 	context = {'object': obj}
# 	return render(request, "tweets/detail_view.html", context)


# def tweet_list_view(request):
# 	obj = Tweet.objects.all()
# 	context = {'object':obj}
# 	return render(request, "tweets/list_view.html", context)
