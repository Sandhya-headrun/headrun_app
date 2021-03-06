
from django.db import models
from django.contrib.auth.models import User

from headrun_community.base.models import BaseModel
# Create your models here.

LOCATION_CHOICES = (
    ("BENGALURU", "BENGALURU"),
    ("HYDERABAD", "HYDERABAD"),
    )
DESIGNATION_CHOICES=(
    ('SE','SE'),
    ('ASE', 'ASE'),
    ('SE','SE'),
    )

class Profile(BaseModel):
    user_id= models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    date_of_birth=models.DateField()
    designation=models.CharField(max_length = 30, choices = DESIGNATION_CHOICES,default='SE')
    work_location=models.CharField(max_length=30,choices = LOCATION_CHOICES,default='HYDERABAD')
    status=models.BooleanField(default=False)

def _str_(self):
    return self.user_name.username
    