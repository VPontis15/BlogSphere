from django.urls import path
from . import views




urlpatterns = [
    path('', views.home, name='home' ),
    path('following', views.following_view, name='following' ),
    path('posts/', views.all_posts, name='posts'),
    path('posts/<slug:slug>/', views.detail_post, name='post'),
    path('new/', views.newPost, name='new'),
    path('edit/<int:id>', views.editPost, name='edit'),
    path('delete/<pk>', views.deletePost, name='delete'),
    path('delete/comment/<pk>', views.deleteComment, name='delete_comment'),
    path('edit/comment/<pk>', views.editComment, name='edit_comment'),
   
   
]
