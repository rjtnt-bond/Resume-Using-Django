from django.urls import path
from serv import views 
urlpatterns = [
    path("serv/",views.serv,name='serv'),
  
]
