from django.db import models
from accounts.models import UserAccounts
from django.db.models.signals import post_delete

from django.contrib.auth import get_user_model
from django.dispatch import receiver

# Create your models here.
class Post(models.Model):
    POST_TYPE = (
    ('software','SOFTWARE'),
    ('web', 'WEB'),
    ('application','APPLICATION'),
    ('marketing','MARKETING'),
    ('other','OTHER'),
)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    ptytle = models.CharField( max_length=20)
    pdescription = models.TextField()
    Ptype = models.CharField(max_length=15, choices=POST_TYPE, default='other')
    create_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)



class Bidd(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="user_bidd")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post_bidd")
    bidd_amt = models.IntegerField()
    bidd_des = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)