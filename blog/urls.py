from django.urls import path
from . import views




urlpatterns = [
    path('', views.home, name='home' ),
    path('posts/', views.all_posts, name='posts'),
    path('posts/<slug:slug>/', views.detail_post, name='post'),
    path('new/', views.newPost, name='new'),
    path('edit/<int:id>', views.editPost, name='edit'),
    path('delete/<pk>', views.deletePost, name='delete'),
   
   
]
