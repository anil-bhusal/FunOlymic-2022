from email import message
from math import fabs
import secrets
from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.db import models
from accounts.models import *

# Create your models here.
class New(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(auto_now_add=True)
    gametype = models.ForeignKey(Gametype, on_delete=models.CASCADE, default=1, null=True)
    title = models.CharField(max_length= 200, default='', null=True, blank=True)
    news = models.TextField( null=False, blank=False)
    image= models.ImageField(upload_to='images_uploaded',null=True)
    news2 = models.TextField( null=True, blank=True)

    @staticmethod
    def get_all_news():
        return New.objects.all()

    @staticmethod
    def get_all_news_by_gametypeid(gametype_id):
        if gametype_id:
             return New.objects.filter(gametype = gametype_id)
        else:
            return New.get_all_news()

    def __str__(self):
        return self.title
        
    def __str__(self):
        return self.title

class Message(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length= 30, default='', null=False, blank=False)
    phone = models.CharField(max_length= 12, default='', null=False, blank=False)
    email = models.CharField(max_length= 100, default='', null=False, blank=False)
    message = models.TextField(max_length= 200, default='', null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)

class Schedule(models.Model):
    id = models.AutoField(primary_key=True)
    game_name = models.CharField(max_length= 30, default='', null=False, blank=False)
    game_date = models.DateField(auto_now_add=False)
    game1 = models.CharField(max_length= 30, default='', null=False, blank=False)
    game2 = models.CharField(max_length= 30, default='', null=True, blank=True)
    game3 = models.CharField(max_length= 30, default='', null=True, blank=True)

    @staticmethod
    def get_all_schedule():
        return Schedule.objects.all()