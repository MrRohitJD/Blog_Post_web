from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
# Create your models here.

class Post(models.Model):
    sno =models.AutoField(primary_key=True)
    author =models.CharField(max_length=100 )
    title =models.CharField(max_length=255)
    category = models.CharField(max_length=200)
    head_0 =models.CharField(max_length=400, blank=True)
    content_0 =models.TextField(max_length=5000, blank=True)
    head_1 =models.CharField(max_length=400, blank=True)
    content_1 =models.TextField(max_length=5000, blank=True)
    head_2 =models.CharField(max_length=400, blank=True)
    content_2 =models.TextField(max_length=5000, blank=True)
    head_3 =models.CharField(max_length=400, blank=True)
    content_3 =models.TextField(max_length=5000, blank=True)
    head_4 =models.CharField(max_length=400, blank=True)
    content_4 = models.TextField(max_length=5000, blank=True)
    timestamp = models.DateTimeField()
    slug =models.CharField(max_length=100)
    image_1= models.ImageField(upload_to="Blog/images", default="", blank=True)
    image_2= models.ImageField(upload_to="Blog/images", default="", blank=True)

    def __str__(self):
        return self.title + ' by ' + self.author
    

class BlogComment(models.Model):
    sno = models.AutoField(primary_key=True)
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post =models.ForeignKey(Post, on_delete=models.CASCADE)
    parent =models.ForeignKey('self', on_delete=models.CASCADE, blank=True)
    timestamp =models.DateTimeField(default=now)

    def __str__(self):
        return self.comment[0:15] + " By " + self.user.username
    