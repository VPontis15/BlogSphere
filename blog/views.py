from django.shortcuts import render
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .models import Post,Tag
# Create your views here.
posts = Post.objects

def home(request):

   user =  request.user.username
   posts = Post.objects
   all_posts = posts.all()
   users_posts = posts.filter(author__username=user)
   not_users_posts = posts.exclude(author__username = user)
   follower_posts = None;
   context = {
      'posts': all_posts,
      'all_posts': all_posts,
      'users_posts': users_posts,
      'not_users_posts': not_users_posts,
      'followers_posts': follower_posts
   }


   return render(request, 'blog/index.html', context)




def all_posts(request):
   q = request.GET.get('q','').strip()
   tag = request.GET.get('tag', '')
   filtered_posts = posts.filter(
    Q(tags__name=tag) |
    Q(tags__name__contains=q) |
    Q(author__username__contains=q) |
    Q(title__contains=q)
).distinct()
   all_posts = posts.all()
   
   context = {
      'all_posts': all_posts,
      'tag': tag,
      'filtered_posts': filtered_posts,
      'search': q
   }

   return render(request, 'blog/posts.html', context)



