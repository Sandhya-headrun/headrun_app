
from datetime import timezone
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
now=timezone.now()

POST_CHOICES = (
    ("STORY", "STORY"),
    ("POST", "POST"),
    )

FILE_CHOICES = (
    ("photo", "photo"),
    ("video", "video"),
    )


LOCATION_CHOICES = (
    ("BENGALURU", "BENGALURU"),
    ("HYDERABAD", "HYDERABAD"),
    )
DESIGNATION_CHOICES=(
    ('Software Engineer','Software Engineer'),
    ('Associate Software', 'Associate Software Engineer'),
    ('Senior Software','Senior Software'),
    )

GENDER_CHOICES= (
    ('MALE','MALE'),
    ('FEMALE', 'FEMALE'),
    ('OTHER', 'OTHER'),
    )
class Profile(models. Model):
    user_id= models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    date_of_birth=models.DateField()
    designation=models.CharField(max_length = 30, choices = DESIGNATION_CHOICES,default='Software Engineer')
    work_location=models.CharField(max_length=30,choices = LOCATION_CHOICES,default='BENGARULU')
    git=models.CharField(max_length=60,null=True )
    phone=models.CharField(max_length=12,null=True )
    gender=models.CharField(max_length = 10,choices = GENDER_CHOICES,default='MALE')
    status=models.BooleanField(default=False)
    

def _str_(self):
    return self.user_name.username
    

class StoriesPosts(models. Model):
    posted_user=models.ForeignKey(User, on_delete=models.CASCADE,null=True, related_name="createdby")
    post_type=models.CharField(max_length=20, choices = POST_CHOICES,default='POST')
    caption = models.TextField(null=True)
    date_posted = models.DateTimeField(default = timezone.now)
    title=models.CharField(max_length=50 ,null=True)
    links=models.URLField(max_length=200, null=True)
    desc=models.TextField(max_length=500, null=True)
    status=models.BooleanField(default=False, null=True)
    created_at=models.DateTimeField(default = timezone.now)
    updated_at=models.DateTimeField(default = timezone.now)
    
class Filetype(models.Model):
    storypost_id=models.ForeignKey(StoriesPosts, on_delete=models.CASCADE,null=True, related_name="storypost_id")
    file_type=models.CharField(max_length = 30, choices = FILE_CHOICES,default='photo')
    # pphoto=models.ForeignKey(StoriesPosts,on_delete=models.CASCADE,null=True, related_name="phots_storiesPost")
    photo=models.FileField(upload_to='static/', null=True, verbose_name="Photo")
    video=models.FileField(upload_to='static/', null=True, verbose_name="Video")
    created_at=models.DateTimeField(default = timezone.now)
    updated_at=models.DateTimeField(default = timezone.now)


class Feedback(models.Model):
    storypostid=models.ForeignKey(StoriesPosts,on_delete=models.CASCADE,null=True, related_name="post_feedbackid")
    feedback=models.TextField(max_length=500 , null=True)
    givenby= models.ForeignKey(User, on_delete=models.CASCADE,null=True, related_name="given_user")
    created_at=models.DateTimeField(default = timezone.now)
    updated_at=models.DateTimeField(default = timezone.now)

class Comments(models.Model):
    comment_by= models.ForeignKey(User,on_delete=models.CASCADE,null=True, related_name="comment_by")
    comment_id= models.ForeignKey(StoriesPosts, on_delete=models.CASCADE,null=True, related_name="post_id")
    comment=models.TextField()
    created_at=models.DateTimeField(default = timezone.now)
    updated_at=models.DateTimeField(default = timezone.now)