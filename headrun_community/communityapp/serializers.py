from argparse import FileType
from dataclasses import field, fields
from rest_framework import serializers
from .models import Profile, StoriesPosts

class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField('user_name')
    class Meta:
        model= Profile
        fields= ['id', 'date_of_birth','designation', 'work_location', 'user' , 'status']
        
    def user_name(self,instance):
        print("self", instance.user_id)
        try:
            return str(instance.user_id)
        except:
            return 0
        
class StoryPostSerializer(serializers.ModelSerializer):

    class Meta:
        model= StoriesPosts
        fields= '__all__'


class FilesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=FileType
        fields='__all__'