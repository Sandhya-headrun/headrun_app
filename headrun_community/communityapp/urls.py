



"""headrun_community URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.contrib.auth.models import User
# from rest_framework import ListCreateAPIView
from .serializers import ProfileSerializer
from .views import *
from communityapp import views
urlpatterns = [
path('users/', UserList.as_view(queryset=Profile.objects.all(), serializer_class=ProfileSerializer), name='user-list'),
path('stories/', StoryPost.as_view(queryset=StoriesPosts.objects.all(), serializer_class=StoryPostSerializer), name='post-list'),
path('get/', StoryPost.as_view(queryset=StoriesPosts.objects.all(), serializer_class=StoryPostSerializer), name='post-list'),
]