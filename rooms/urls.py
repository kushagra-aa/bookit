from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('login/', views.login, name='login'),
    path('handleLogin/', views.handleLogin, name='handleLogin'),
    path('signup/', views.signup, name='signup'),
    path('handleSignup/', views.handleSignup, name='handleSignup'),
    path('logout/', views.handleLogout, name='logout'),
    path('view-rooms/', views.rooms, name='view-rooms'),
    path('room/', views.room, name='room'),
    path('seller/', views.seller, name='seller')
]
