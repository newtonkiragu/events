from django.conf.urls import url
from django.contrib.auth import login
from django.contrib.auth.views import LogoutView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import path, include

from epa_frontend.views import views, authentication, merchants, events, events_type

urlpatterns = [
    url('^$', views.home, name='index'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile/', authentication.view_profile, name='view_profile'),
    path('accounts/profile/update/', authentication.update_profile, name='update_profile'),
    path('accounts/signup/', authentication.signup, name='signup'),
    # path('accounts/login/', login, name='login'),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
    path('password-reset/', authentication.password_reset, name='password_reset'),
    path('password-reset-confirm/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         PasswordResetCompleteView.as_view(template_name='registration/password_reset/password_reset_complete.html'),
         name='password_reset_complete'),
    path('merchants/new/', merchants.create_merchant, name='create_merchant'),
    path('merchants/', merchants.view_merchants, name='view_merchants'),
    path('merchant/<int:pk>/', merchants.view_merchant, name='view_merchant'),
    path('merchant/<int:pk>/update/', merchants.update_merchant, name='update_merchant'),
    path('events/', events.view_events, name='view_events'),
    path('events/new/', events.create_event, name='create_events'),
    path('about/', views.view_about, name='view_about'),
    path('event/<str:slug>/', events.view_event, name='view_event'),
    path('event/<str:slug>/edit', events.edit_event, name='edit_event'),
    path('event/<str:slug>/publish/', events.publish_event, name='publish_event'),
    path('event/<str:slug>/un-publish/', events.un_publish_event, name='un_publish_event'),
    path('event/<str:slug>/dashboard/', events.view_event_dashboard, name='view_event_dashboard'),
    path('event-type/<int:pk>/', events_type.view_event_type, name='view_event_type'),
    path('event-type/new/', events_type.create_event_type, name='create_event_type'),
]
