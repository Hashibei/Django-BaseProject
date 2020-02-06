from django.urls import path
from django.contrib.auth import views as auth_views
from account import views as account_views


urlpatterns = [
    path('login',
         auth_views.LoginView.as_view(
             template_name='account/login.html',
             extra_context={
                 'title': 'Account login'}),
         name='login'),

    path('logout',
         auth_views.LogoutView.as_view(
             template_name='account/logout.html',
             extra_context={
                 'title': 'Account logout'}),
         name='logout'),

    path('register',
         auth_views.LoginView.as_view(
             template_name='account/register.html',
             extra_context={
                 'title': 'Account register'}),
         name='register'),

    path('profile',
         account_views.ProfileView.as_view(),
         name='profile'),

    path('profile/edit',
         account_views.ProfileEditView.as_view(),
         name='profile_edit'),

    path('password_change',
         auth_views.PasswordChangeView.as_view(
             template_name='account/password_change.html',
             extra_context={
                 'title': 'Account password change'}),
         name='password_change'),

    path('password_change/done',
         auth_views.PasswordChangeDoneView.as_view(
             template_name='account/password_change_done.html',
             extra_context={
                 'title': 'Account change password done'}),
         name='password_change_done'),

    path('password_reset',
         auth_views.PasswordResetView.as_view(
             template_name='account/password_reset.html',
             extra_context={
                 'title': 'Account change password reset'}),
         name='password_reset'),

    path('password_reset/done',
         auth_views.PasswordResetDoneView.as_view(
             template_name='account/password_reset_done.html',
             extra_context={
                 'title': 'Account change password done'}),
         name='password_reset_done'),

    path('password_reset/confirm',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='account/password_reset_confirm.html',
             extra_context={
                 'title': 'Account change password confirm'}),
         name='password_reset_confirm'),

    path('password_reset/complete/<uidb64>/<token>/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='account/password_reset_complete.html',
             extra_context={
                 'title': 'Account change password complete'}),
         name='password_reset_complete')
]
