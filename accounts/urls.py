from django.urls import path
from . import views



urlpatterns =[ 
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutPage, name='logout'),
    path('register/', views.register, name='register'),
    path('success/', views.success, name='success'),
    path('user/<str:username>/<str:tab>', views.viewProfile, name='user-profile')
]