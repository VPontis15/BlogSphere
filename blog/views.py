from django.shortcuts import redirect, render, get_object_or_404
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .models import Post,Tag,Comment
from .forms import PostForm, CommentForm
from accounts.models import Profile
from django.contrib import messages
# Create your views here.

posts = Post.objects

@login_required(login_url='login')
def home(request):
    user_profile = None
    users_posts = not_users_posts = following_posts = all_posts = None

    if request.user.is_authenticated:
        try:
            user_profile = Profile.objects.get(user=request.user)
        except Profile.DoesNotExist:
            user_profile = None

        if user_profile:
            user = request.user.username
            following_posts = Post.objects.filter(author__profile__in=user_profile.following.all()).exclude(author=request.user)
            users_posts = Post.objects.filter(author__username=user)
            not_users_posts = Post.objects.exclude(author__username=user)

    all_posts = Post.objects.all()

    context = {
        'posts': all_posts,
        'all_posts': all_posts,
        'users_posts': users_posts,
        'not_users_posts': not_users_posts,
        'user_profile': user_profile,
        'following_posts': following_posts,
    }

    return render(request, 'blog/index.html', context)




def all_posts(request):
   q = request.GET.get('q', '').strip()
   tag = request.GET.get('tag', '')
   filter_param = request.GET.get('filter', '')
   all_posts = posts.all()
   filtered_posts_by_author = posts.filter(author__username__contains=q)
   filtered_posts_by_title =all_posts.filter(title__icontains=q)
   filtered_posts_by_tag = posts.filter(Q(tags__name__contains=q)| Q(tags__name = tag)).distinct()
   if q:
      filtered_posts = posts.filter(
      Q(tags__name=tag) |
      Q(tags__name__icontains=q) |
      Q(author__username__icontains=q) |
      Q(slug__icontains=q)
   ).distinct()
   else: 
      filtered_posts = None;
   tag_posts = posts.filter(tags__name = tag)
   

   
   
   context = {
      'all_posts': all_posts,
      'tag': tag,
      'filter': filter_param,
      'filtered_posts': filtered_posts,
      'search': q,
      'tag_posts': tag_posts,
      "filtered_posts_by_author": filtered_posts_by_author,
      "filtered_posts_by_title": filtered_posts_by_title,
      "filtered_posts_by_tag": filtered_posts_by_tag

   }

   return render(request, 'blog/posts.html', context)





def detail_post(request, slug):
   post = posts.get(slug = slug)
   if request.method == "POST":
      form = CommentForm(request.POST, instance= request.user.profile)
      if form.is_valid():
       comment = form.save(commit=False)
       comment.user = request.user.profile
       comment.save()
       form.save_m2m();
       return redirect('post', slug=slug)
      else: 
            redirect('post', slug=slug)
   else:
      form = CommentForm()
   context = {
      'post': post
   }
   return render(request, 'blog/post.html', context  )


@login_required(login_url='login')
def newPost(request):
   if request.method == 'POST':
      form = PostForm(request.POST)
      if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        form.save_m2m()
        return redirect('home')
      
   else:
      form = PostForm()
   return render(request, 'blog/new.html', {
      'form': form
   })

@login_required(login_url= 'login')
def deletePost(request, pk):
   post = posts.get(pk = pk)

   if request.method == "POST":
      post.delete()
      messages.info(request, 'Your post has been successfully deleted', extra_tags='sucess-delete--post')
      return redirect('home')
   context = {
      'post': post,
      'id': id
   }
   return render(request, 'layout.html', context )



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






