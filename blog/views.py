from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Post
# Create your views here.


def home(request):
   user =  request.user.username
   posts = Post.objects
   all_posts = posts.all()
   users_posts = posts.filter(author__username=user)
   not_users_posts = posts.exclude(author__username = user)
   follower_posts = None;
   context = {
      'all_posts': all_posts,
      'users_posts': users_posts,
      'not_users_posts': not_users_posts,
      'followers_posts': follower_posts
   }


   return render(request, 'blog/index.html', context)



