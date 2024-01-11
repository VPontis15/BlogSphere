from django.shortcuts import render,redirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .models import Post,Tag
from .forms import PostForm
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



def newPost(request):
   if request.method == 'POST':
      form = PostForm(request.POST)
      if form.is_valid():
         post = form.save(commit=False)
         post.author = request.user
         post.save()
         render(request, 'blog/sucess.html')
   else:
         form = PostForm()
   context = {
      'form': form
   }
   return render(request, 'blog/new.html', context)



def detailsPost(request,slug):
   post = posts.get(slug = slug)
   context = {
     'post': post
   }
   return render(request, 'blog/post.html', context)
