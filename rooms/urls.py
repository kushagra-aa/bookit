from django.urls import path
from . import views

app_name = 'rooms'
urlpatterns = [
    path('', views.index, name='home'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('handleLogin/', views.handleLogin, name='handleLogin'),
    path('handleSignup/', views.handleSignup, name='handleSignup'),
    path('handleRoom/', views.handleRoom, name='handleRoom'),
    path('logout/', views.handleLogout, name='logout'),
    path('view-rooms/', views.rooms, name='view-rooms'),
    path('<int:room_id>', views.room, name='room'),
    path('add-room/', views.addRoom, name='add-room'),
    path('<str:seller_id>', views.seller, name='seller')
]
