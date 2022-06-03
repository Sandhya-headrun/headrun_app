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

from django.urls import path,include
from user.api.serializers import PostSerializer, ProfileSerializer
from user.models.models import Posts,Profile
from user.views import StoryPost, UserList
urlpatterns = [

    path('users/', UserList.as_view(queryset=Profile.objects.all(), serializer_class=ProfileSerializer), name='user-list'),
    path('users/', StoryPost.as_view(queryset=Posts.objects.all(), serializer_class=PostSerializer), name='posts-list'),
]