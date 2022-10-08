from re import T
from turtle import title
from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.utils.timezone import localtime
from django.utils import timezone
from django.core.validators import FileExtensionValidator
from django.utils.timezone import now


class Profile(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    auth_token = models.CharField(max_length=100 )
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class Gametype(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    @staticmethod
    def get_all_gametypes():
        return Gametype.objects.all()
    def __str__(self):
        return self.name


class Game(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length= 200, default='', null=True, blank=True)
    desc = models.CharField(max_length=10000, default='', null=True, blank=True)
    gametype = models.ForeignKey(Gametype, on_delete=models.CASCADE, default=1, null=True)
    image = models.ImageField(upload_to='images_uploaded',null=True)
    video = models.FileField(upload_to='videos_uploaded',null=True,validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])
    date_uploaded = models.DateTimeField(default=timezone.now)   
    likes = models.ManyToManyField(User, blank=True, related_name='likes')
    dislikes = models.ManyToManyField(User, blank=True, related_name='dislikes')

    @staticmethod
    def get_all_games():
        return Game.objects.all()
    @staticmethod
    def get_all_games_by_gametypeid(gametype_id):
        if gametype_id:
             return Game.objects.filter(gametype = gametype_id)
        else:
            return Game.get_all_games()
    def __str__(self):
        return self.title

class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Game', null=False, blank=False, on_delete=models.CASCADE)
    comment = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.user.username

