from django.urls import path
from . import views




urlpatterns = [
    path('', views.home, name='home' ),
    path('posts/', views.all_posts, name='posts'),
    path('new', views.newPost, name='new'),
    path('post/<slug:slug>', views.detailsPost, name='post')
   
]
