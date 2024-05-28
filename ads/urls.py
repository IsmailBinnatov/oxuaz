from django.urls import path, include
from .views import index, indexFeed

urlpatterns = [
    path('', index),
    path('<int:id>/', indexFeed),
]