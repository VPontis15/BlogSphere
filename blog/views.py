from django.shortcuts import redirect, render, get_object_or_404
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .models import Post,Tag
from .forms import PostForm
from accounts.models import Profile
# Create your views here.
posts = Post.objects

def home(request):
   try:
        user_profile = Profile.objects.get(user=request.user)
   except Profile.DoesNotExist:
       
        user_profile = None
   user =  request.user.username
   if user_profile:
      following_posts = Post.objects.filter(author__profile__in = user_profile.following.all()).exclude(author = request.user)
   
   all_posts = posts.all()
   users_posts = posts.filter(author__username=user)
   
   not_users_posts = posts.exclude(author__username = user)
   
   context = {
      'posts': all_posts,
      'all_posts': all_posts,
      'users_posts': users_posts,
      'not_users_posts': not_users_posts,
       "user_profile": user_profile,
       "following_posts": following_posts
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


def detail_post(request, slug):
   post = posts.get(slug = slug)
   context = {
      'post': post
   }
   return render(request, 'blog/post.html', context  )



def newPost(request):
   if request.method == 'POST':
      form = PostForm(request.POST)
      if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        return redirect('home')
      
   else:
      form = PostForm()
   return render(request, 'blog/new.html', {
      'form': form
   })

@login_required(login_url= 'login')
def deletePost(request, id):
   post = posts.get(pk = id)

   if request.method == "POST":
      post.delete()
      return redirect('home')
   context = {
      'post': post,
      'id': id
   }
   return render(request, 'components/delete.html', context )



def editPost(request, id):
   post = posts.get(pk = id)

   if request.method == "POST":
      form = PostForm(request.POST,instance= post)
      if form.is_valid():
         form.save()
         return redirect('home')
   else:
      form = PostForm(instance=post)

   context = {
      "form": form,
      "id": id
   }

   return render(request, 'blog/new.html', context)



