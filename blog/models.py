from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE) 
    # on_delete=models.CASCADE  if the user get deleted, the post is deleted aswell

    #this fucntion returns how the post is printed out
    def __str__(self):
        return self.title


