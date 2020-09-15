from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.utils.timezone import now

# Create your models here.

class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=300)
    content = models.TextField()
    author = models.CharField(max_length=40)
    slug = models.CharField(max_length=200)
    views = models.IntegerField(default=0)
    timeStamp = models.DateTimeField(blank=True)

    def __str__(self):
        return "Post from " + self.title + " with title " + self.title
         

class BlogComment(models.Model):
    sno = models.AutoField(primary_key=True)
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    timeStamp = models.DateTimeField(default=now)

    def __str__(self):
        return self.user.username + " says : " + self.comment