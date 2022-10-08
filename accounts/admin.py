from django.contrib import admin 
from .models import Profile
from .models import Gametype, Game, Comment
from .models import User
# from .models import  Product, Category
# Register your models here.

from embed_video.admin import AdminVideoMixin
# from .models import Video

class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

# admin.site.register(Video, MyModelAdmin)

# class UserAdmin(admin.ModelAdmin):
#     # list_display:('username', 'email', 'is_staff')
# admin.site.register(User, UserAdmin)

admin.site.site_header = 'FunOlympics'
admin.site.register(Profile)


class AdminContent(admin.ModelAdmin):
    list_display = ['title', 'desc', 'gametype']

class AdminGametype(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Game, AdminContent)
admin.site.register(Gametype, AdminGametype)

admin.site.register((Comment))





