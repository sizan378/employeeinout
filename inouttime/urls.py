
from django.urls import path
from .views import *

urlpatterns = [
   
    path('', index, name='profile'),
    path('login/', getLogin, name='login'),
    path('logout/', getLogout, name='logout'),
    path('attend/', attend, name='attend'),
    path('outtime/', OutTime, name='outtime'),
    
 
]