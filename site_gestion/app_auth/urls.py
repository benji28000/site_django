from django.urls import path
from .views import *

urlpatterns=[
    path('login/',login_site, name="login-site"),
    path('register/',register,name='register'),
    path('deconnexion/',deconnexion,name='deconnexion'),


]