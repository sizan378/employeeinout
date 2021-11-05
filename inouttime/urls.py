
from django.urls import path
from .views import *

urlpatterns = [
   
    path('', index, name='index'),
    path('login/', getLogin, name='login'),
    path('logout/', getLogout, name='logout'),
    path('attend/', attend, name='attend'),
    path('outtime/', OutTime, name='outtime'),
    path('support/', getSupport, name='support'),
    # path('employee/<name>', getEmployee, name='employee')
    
 
]