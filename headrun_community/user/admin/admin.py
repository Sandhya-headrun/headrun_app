from argparse import FileType
from django.contrib import admin
from user.models.models import Feedback, Profile, Posts,Comments,Likes
# Register your models here.

admin.site.register(Profile)
admin.site.register(Posts)
admin.site.register(Likes)
admin.site.register(Comments)
admin.site.register(Feedback)