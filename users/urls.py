from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    
    path('signup/', views.signup, name='signup'),
    path('login/', views.login1, name='login'),
]