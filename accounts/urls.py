from django.contrib import admin
from django.urls import include, path, re_path
from .views import *
from . import views
from django.contrib.auth import views as auth_views
from accounts.views import Description
from django.conf.urls import handler400

urlpatterns = [
    path('home' ,  home, name="home"), 
    path('news' ,  news, name="news"),
    path('schedule' ,  schedule, name="schedule"),
    path('newsdesc/<int:pid>' ,  newsdesc, name="newsdesc"),    
    path('register', register_attempt , name="register_attempt"),
    path('login', login_attempt , name="login_attempt"),
    path('token', token_send , name="token_send"),
    path('success', success , name='success'),
    path('verify/<auth_token>' , verify , name="verify"),
    path('error', error_page , name="error"),
    path('logout', views.logout_functions, name="logout"),
    path('password_reset/',auth_views.PasswordResetView.as_view(template_name= 'password_reset.html'),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name= 'password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name= 'password_reset_confirm.html'),name='password_reset_confirm'),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name= 'password_reset_complete.html'),name='password_reset_complete'),
    path('changepass/', views.user_change_pass, name="changepass"),
    path('description/<int:pid>', Description.as_view(), name='desc'),
    path('search-games/', views.BlogSearchView.as_view(), name='search_games'),
    path('post/<int:pk>/like', AddLike.as_view(), name='like'),
    path('post/<int:pk>/dislike', AddDislike.as_view(), name='dislike'),
]
handler400= 'accounts.views.error_404'