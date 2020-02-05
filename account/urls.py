from django.urls import path
from django.contrib.auth.views import *
from account.views import *


urlpatterns = [
    path('login',
         LoginView.as_view(
             template_name='account/login.html',
             extra_context={
                 'title': 'Account login'}),
         name='login'),

    path('logout',
         LogoutView.as_view(
             template_name='account/logout.html',
             extra_context={
                 'title': 'Account logout'}),
         name='logout'),

    path('register',
         LoginView.as_view(
             template_name='account/login.html',
             extra_context={
                 'title': 'Account register'}),
         name='register'),

    path('profile',
         ProfileView.as_view(
             template_name='account/profile.html',
             extra_context={
                 'title': 'Account profile'}),
         name='profile'),

    path('password_change',
         PasswordChangeView.as_view(
             template_name='account/password_change.html'),
         name='password_change'),

    path('password_change/done',
         PasswordChangeDoneView.as_view(
             template_name='account/password_change_done.html'),
         name='password_change_done'),

    path('password_reset',
         PasswordResetView.as_view(
             template_name='account/password_reset.html'),
         name='password_reset'),

    path('password_reset/done',
         PasswordResetDoneView.as_view(
             template_name='account/password_reset_done.html'),
         name='password_reset_done'),

    path('password_reset/confirm',
         PasswordResetConfirmView.as_view(
             template_name='account/password_reset_confirm.html'),
         name='password_reset_confirm'),

    path('password_reset/complete/<uidb64>/<token>/',
         PasswordResetCompleteView.as_view(
             template_name='account/password_reset_complete.html'),
         name='password_reset_complete')
]