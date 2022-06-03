
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
LOCATION_CHOICES = (
    ("BENGALURU", "BENGALURU"),
    ("HYDERABAD", "HYDERABAD"),
    )
DESIGNATION_CHOICES=(
    ('SE','SE'),
    ('ASE', 'ASE'),
    ('SE','SE'),
    )


class Profile(models. Model):
    user_id= models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    date_of_birth=models.DateField()
    designation=models.CharField(max_length = 30, choices = DESIGNATION_CHOICES,default='SE')
    work_location=models.CharField(max_length=30,choices = LOCATION_CHOICES,default='BENGARULU')
    status=models.BooleanField(default=False)
    

def _str_(self):
    return self.user_name.username
    

class Posts(models. Model):
    post_type=models.CharField(max_length = 30, choices = POST_CHOICES,default="POST")
    posted_username=models.ForeignKey(User, on_delete=models.CASCADE,null=True, related_name="createdby")
    date_posted = models.DateTimeField(default = timezone.now)
    photo=models.ImageField(upload_to='static/', null=True, verbose_name="Photo")
    video=models.FileField(upload_to='static/', null=True, verbose_name="Video")
    description=models.TextField(max_length=500, null=True)
    tags=models.CharField(max_length=50 ,null=True)
    links=models.URLField(max_length=200, null=True)
    status=models.BooleanField(default=False, null=True)
    created_at=models.DateTimeField(default = timezone.now)
    updated_at=models.DateTimeField(default = timezone.now)
    

class Comments(models.Model):
    comment_by= models.ForeignKey(User,on_delete=models.CASCADE,null=True, related_name="comment_by")
    post_id= models.ForeignKey(Posts, on_delete=models.CASCADE,null=True, related_name="post_id")
    comment=models.TextField()
    comment_date=models.DateTimeField(default = timezone.now)
    status=models.BooleanField(default=False, null=True)
    created_at=models.DateTimeField(default = timezone.now)
    updated_at=models.DateTimeField(default = timezone.now)
    
class Likes(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True, related_name="liked_by")
    liked_post=models.ForeignKey(Posts,User,on_delete=models.CASCADE,null=True, related_name="liked_post")
    status=models.BooleanField(default=False, null=True)
    created_at=models.DateTimeField(default = timezone.now)
    updated_at=models.DateTimeField(default = timezone.now)

class Feedback(models.Model):
    postid=models.ForeignKey(Posts,on_delete=models.CASCADE,null=True, related_name="post_feedbackid")
    feedback=models.TextField(max_length=500 , null=True)
    givenby= models.ForeignKey(User, on_delete=models.CASCADE,null=True, related_name="given_user")
    created_at=models.DateTimeField(default = timezone.now)
    updated_at=models.DateTimeField(default = timezone.now)