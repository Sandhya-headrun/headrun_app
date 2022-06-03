from django.shortcuts import render
from headrun_community.user.api.serializers import ProfileSerializer,PostSerializer
from models.models import Profile, Posts
#from user.serializers import ProfileSerializer, StoryPostSerializer
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
# Create your views here.
class UserList(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAdminUser]

    def list(self, request):
        queryset = self.get_queryset()
        serializer = ProfileSerializer(queryset, many=True)
        return Response(serializer.data)
    
class StoryPost(generics.ListCreateAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)
    