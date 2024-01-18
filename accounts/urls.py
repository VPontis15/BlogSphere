from django.urls import path
from . import views
from blog.views import detail_post


urlpatterns =[ 
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutPage, name='logout'),
    path('register/', views.register, name='register'),
    path('success/', views.success, name='success'),
    path('user/<str:username>/<str:tab>', views.viewProfile, name='user-profile'),
    path('MyProfile/', views.myProfile, name='editProfile'),
    path('follow/', detail_post, name='follow')
  
]