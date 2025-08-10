from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'feed'
urlpatterns = [
    path('',views.home, name='home'),
    path('explore/',views.explore, name='explore'),
    path('login/',auth_views.LoginView.as_view(template_name='feed/login.html')),

]