from atexit import register
import imp
from importlib.resources import contents
from django.forms import ValidationError
from django.http import HttpResponseRedirect
from urllib3 import HTTPResponse
from accounts.models import Profile, Game, Gametype
from django.shortcuts import redirect, render, reverse
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm, AuthenticationForm
from django.contrib import messages
import requests 
from django.shortcuts import get_object_or_404
import json
from .models import *
from funolympicgame2022.models import *
import uuid
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import authenticate,login , logout , update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.views import View 
from django.db.models import Q
from .serializer import *
import warnings
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


warnings.filterwarnings(action= 'ignore')

def error_404(request, exception):
    return render(request, '404.html')


def login_attempt(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user_obj = User.objects.filter(username=username).first()
        if  user_obj is None:
            messages.success(request, 'Username doesnot exist!')
            return redirect('/login')
        
        profile_obj = Profile.objects.filter(user= user_obj).first()

        if not profile_obj.is_verified:
            messages.success(request, 'Your account is not verified, please check your mail.')
            return redirect('/login')

        user = authenticate(username=username, password=password)
        if user is None:
            messages.success(request, 'Username or password is wrong!')
            return redirect('/login')
        
        login(request, user)
        
        # for capctha 
        clientKey =  request.POST['g-recaptcha-response']
        secretKey =  '6LffCGkgAAAAAHU3tqei4M-Pka1tlO8ZG_Dz-pWo'
        captchaData = {
            'secret': secretKey,
            'response': clientKey
        }    
        r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=captchaData)
        response = json.loads(r.text)
        verify = response['success']
        if verify:
            return redirect('/home')
           
        else:
            messages.success(request, 'Captcha is not filled!')
            return render(request , 'login.html')

    return render(request, 'login.html')


def register_attempt(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        conPassword = request.POST.get('conPassword')

        if User.objects.filter(username=username).first():
            messages.error(request, 'Username already exist!')
            return redirect('/register')
            
        if len(username) > 10:
            messages.success(request, "Username must be under 10 character")
            return redirect('/register')

        if len(username) < 5:
            messages.success(request, "Username must be minimum 5 character long")
            return redirect('/register')

        if User.objects.filter(email = email).first():
            messages.success(request, 'Email already exist!')
            return redirect('/register')
        try:                
            #captcha
            clientKey =  request.POST['g-recaptcha-response']
            secretKey =  '6LffCGkgAAAAAHU3tqei4M-Pka1tlO8ZG_Dz-pWo'
            captchaData = {
                'secret': secretKey,
                'response': clientKey
            }    
            r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=captchaData)
            response = json.loads(r.text)
            verify = response['success']
            print('Your success is: ', verify)
            if verify:

                if len(password) < 8:
                    messages.success(request, "Password must 8 character long")
                    return redirect('/register')
        
                # check for digit in password
                if not any(char.isdigit() for char in password):
                    messages.success(request, "Password must contain atleast 1 digit")
                    return redirect('/register')
                
                # check for letter
                if not any(char.isalpha() for char in password):
                    messages.success(request, "Password must contain atleast 1 alphabet")
                    return redirect('/register')

                #checking password
                if password != conPassword:
                    messages.success(request, 'Password doesnot match!')
                    return redirect('/register')

                if(password == username):
                    messages.success(request, 'password is similar to username')
                    return redirect('/register')


                if(password == email):
                    messages.success(request, 'password is similar to email')
                    return redirect('/register')

                user_obj = User(username=username, email=email)
                user_obj.set_password(password)
                user_obj.save()

                auth_token = str(uuid.uuid4())
                profile_obj = Profile.objects.create(user = user_obj, auth_token=auth_token)
                profile_obj.save()
                send_mail_after_registration(email, auth_token)
                return redirect('/token')
                # return render(request , 'token_send.html')
            else:
                messages.success(request, 'Captcha is not filled!')
                return render(request , 'register.html')

        except Exception as e:
            print(e)
        
    return render(request, 'register.html')


def success(request):
    return render(request , 'success.html')


def token_send(request):
    return render(request , 'token_send.html')


def password_reset(request):
    return render(request, 'password_reset_confirm.html' )


def verify(request , auth_token):
    try:
        profile_obj = Profile.objects.filter(auth_token = auth_token).first()

        if profile_obj:
            if profile_obj.is_verified:
                messages.success(request, 'Your account is already verified.')
                return redirect('/login')
            profile_obj.is_verified = True
            profile_obj.save()
            messages.success(request, 'Your account has been verified.')
            return redirect('/login')
        else:
            return redirect('/error')
    except Exception as e:
        print(e)
        return redirect('/home')


def send_mail_after_registration(email , token):
    subject = 'Your accounts need to be verified'
    message = f'Hi, click or paste this link to newtab to verify your account: http://127.0.0.1:8000/verify/{token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message , email_from ,recipient_list )


def error_page(request):
    return  render(request , 'error.html')


def PasswordResetConfirmView(request):
    return redirect(request, 'login')

# for logout:
def logout_functions(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/')
        
    request.session.clear()
    return redirect('/')

@login_required(login_url = "/login") 
def user_change_pass(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('/home')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'changepass.html', {'form': form })


#Home page
@login_required(login_url = "/login")   
def home(request):
    gametypes = Gametype.get_all_gametypes()
    gametypeID = request.GET.get('gametype')
    conDesc = Game.get_all_games()
    newsin = New.get_all_news()
    if gametypeID:
            contents = Game.get_all_games_by_gametypeid(gametypeID)
            news = New.get_all_news_by_gametypeid(gametypeID)
    else:
        contents = Game.get_all_games()
        news= New.get_all_news()

    data = {'contents': contents, 'gametypes': gametypes, 'conDesc':conDesc, 'newsin':newsin, 'news': news}
    return render(request, 'home.html', data)


#Search
class BlogSearchView(LoginRequiredMixin, ListView):
    login_url = '/login'
    redirect_field_name = 'login'
    model = Game
    template_name = 'search.html'
    context_object_name = 'contents'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Game.objects.filter(title__icontains=query).order_by('-date_uploaded')


# description page
class Description(LoginRequiredMixin, View):
    login_url = '/login'
    redirect_field_name = 'login'

    def get(self, request, pid, *args, **kwargs):
        # contents = Content.objects.get(id=pid)
        contents = get_object_or_404(Game, id=pid)
        conDesc = Game.get_all_games()
        conLike= contents.likes
        post_comments_count = Comment.objects.all().filter(post=pid).count()
        post_comments = Comment.objects.all().filter(post=pid)
        return render(request, 'description.html', {'content': contents, 'conDesc': conDesc, 'post_comments_count':post_comments_count, 'post_comments':post_comments, 'conLike': conLike})
    
    def post(self, request, pid, *args, **kwargs):
        if request.method == 'POST':
            com = request.POST.get('comment')
            comments = Comment()
            contents = Game.objects.get(id=pid)
            comments.user = self.request.user
            comments.post = contents
            comments.comment = com
            comments.save()
            return redirect("desc", pid)

# like and dis-like
class AddLike(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        post = Game.objects.get(pk=pk)
        is_dislike = False
        for dislike in post.dislikes.all():
            if dislike == request.user:
                is_dislike = True
                break
        if is_dislike:
            post.dislikes.remove(request.user)
        is_like = False
        for like in post.likes.all():
            if like == request.user:
                is_like = True
                break
        if not is_like: 
            post.likes.add(request.user)
        
        if is_like:
            post.likes.remove(request.user)
        
        next = request.POST.get('next', '/home')
        return HttpResponseRedirect(next)

class AddDislike(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        post = Game.objects.get(pk=pk)
        is_like = False
        for like in post.likes.all():
            if like == request.user:
                is_like = True
                break
        if is_like:
            post.likes.remove(request.user)
        is_dislike = False
        for dislike in post.dislikes.all():
            if dislike == request.user:
                is_dislike = True
                break
        if not is_dislike: 
            post.dislikes.add(request.user)
        
        if is_dislike:
            post.dislikes.remove(request.user)
        
        next = request.POST.get('next', '/home')
        return HttpResponseRedirect(next)

# news
@login_required(login_url = "/login")  
def news(request, *args, **kwargs):
    news = New.get_all_news()
    return render(request, 'news.html', {'news': news})

@login_required(login_url = "/login")  
def newsdesc(request, pid, *args, **kwargs):
    news2 = get_object_or_404(New, id=pid)
    newsDesc1 = New.get_all_news()
    return render(request, 'newsdesc.html', {'new': news2, 'newsDesc1': newsDesc1})

@login_required(login_url = "/login")  
def schedule(request, *args, **kwargs):
    schedule1 = Schedule.get_all_schedule()
    return render(request, 'schedule.html', {'schedule': schedule1})

