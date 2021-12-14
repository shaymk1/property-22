

from django.urls import path
from . import views

urlpatterns =[
    path('contact', views.contact, name='contact'),
    # path('login', views.login, name='login'),
    # path('logout', views.logout, name='logout'),
    # path('dashboard', views.dashboard, name='dashboard'),
   
    
]
