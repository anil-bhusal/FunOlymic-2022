from django.contrib import admin
from .models import New, Message, Schedule

# Register your models here.
admin.site.register((New))
admin.site.register((Message))
admin.site.register((Schedule))
