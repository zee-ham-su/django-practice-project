from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model): 
    title = models.CharField(max_length=100) # max_length is a required field
    content = models.TextField()  # TextField is a required field
    date_posted = models.DateTimeField(default=timezone.now) # auto_now_add is a required field
    author = models.CharField(max_length=100) # max_length is a required field

    def __str__(self): 
        return self.title # This will return the title of the post in the admin panel
