from django.http import HttpResponse
from django.shortcuts import render
from .models import Feed

# Create your views here.


def index(request):
    feeds = Feed.objects.all()
    context = {'feeds': feeds}
    return render(request, 'ads/index.html', context)


def indexFeed(request, id):
    return render(request, 'ads/detail.html')
