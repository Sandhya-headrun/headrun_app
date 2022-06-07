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
from userapp.api.serializers import PostSerializer, ProfileSerializer
from userapp import views
from userapp.model.models import Posts,Profile
from userapp.api.views import GetPosts, UserList,GetStory,EventDetails
urlpatterns = [

    path('users/', UserList.as_view(queryset=Profile.objects.all(), serializer_class=ProfileSerializer), name='user-list'),
    path('posts/', GetPosts.as_view(), name='posts-list'),
    path('stories/', GetStory.as_view(), name='posts-list'),
    path('update/<int:id>/', views.updatepost, name="updatepost"),
    path('delete/<int:id>/', views.delete_post, name="deletepost"),
    path('updatestory/<int:id>/', views.updatestory, name="updatestory"),
    path('deletestory/<int:id>/', views.delete_story, name="deletestory"),
    path('events/', EventDetails.as_view(), name='Events'),
    path('updateEvent/<int:id>/', views.updateEvent, name="updatestory"),
    path('deleteEvent/<int:id>/', views.deleteEvent, name="deletestory"),
]