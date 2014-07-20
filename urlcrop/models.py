from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Url(models.Model):
    # id = models.AutoField(primary_key=True)
    actual_url = models.URLField(max_length=1000)
    url_hash = models.CharField(max_length=512)
    shortened_url = models.CharField(max_length=1000)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    valid_for_days = models.IntegerField(default=60)
    user = models.ForeignKey(User, null=True)
    
    

