from argparse import FileType
from django.contrib import admin
from .models import Feedback, Filetype, Profile,StoriesPosts,Feedback
# Register your models here.

admin.site.register(Profile)
admin.site.register(StoriesPosts)
admin.site.register(Filetype)
admin.site.register(Feedback)