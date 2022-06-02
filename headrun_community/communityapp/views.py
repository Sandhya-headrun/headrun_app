import time
from django.shortcuts import render
from .models import Profile, StoriesPosts
from communityapp.serializers import ProfileSerializer, StoryPostSerializer
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
    queryset = StoriesPosts.objects.all()
    serializer_class = StoryPostSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = StoryPostSerializer(queryset, many=True)
        return Response(serializer.data)
    
    
