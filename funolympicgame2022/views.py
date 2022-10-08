
import email
from email import message
from django.shortcuts import render
from accounts.models import Profile, Game, Gametype
from django.shortcuts import redirect, render, reverse
from django.contrib.auth.models import User
from .models import *
from django.views import View
from django.shortcuts import get_object_or_404


def index(request, *args, **kwargs):
    news = New.get_all_news()
    schedule = Schedule.get_all_schedule()
    newsDesc = New.get_all_news()
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')
        messages = Message(name= name, phone = phone, email= email, message= message)
        messages.save()
        return redirect("index")
    return render(request, 'index.html', {'news': news, 'newsDesc':newsDesc, 'schedule':schedule})


def schedule(request):
    return render(request, 'index.html')




def latestnews(request, pid, *args, **kwargs):
    new1 = get_object_or_404(New, id=pid)
    newsDesc = New.get_all_news()
    return render(request, 'latestnews.html', {'new': new1, 'newsDesc': newsDesc})


