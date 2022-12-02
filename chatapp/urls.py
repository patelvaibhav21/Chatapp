from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('roomof/<str:yourname>/', views.frontend, name='frontend'),
    path('checkview', views.checkview, name='checkview'),
    path('send', views.send, name='send'),
    path('getMessages/<str:friendname>/', views.frdMessages, name='friendname'),
    path('myMessages/<str:myname>/', views.myMessages, name='myMessages'),
]