from django.shortcuts import redirect, render, get_object_or_404
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .models import Post, Tag, Comment, Like,Notification
from .forms import PostForm, CommentForm
from accounts.models import Profile
from django.contrib import messages
from django.db.models import Count
# Create your views here.

posts = Post.objects


@login_required(login_url='login')
def home(request):
    user_profile = None
    tags = Tag.objects.all()


    all_posts = Post.objects.all().distinct().order_by('-created_at')
    popular_posts = Post.objects.annotate(num_likes=Count('likes')).order_by('-num_likes')[:3]
    context = {
        'posts': all_posts,
        'user_profile': user_profile,
        'tags': tags,
        'popular_posts': popular_posts
    }

    return render(request, 'blog/index.html', context)

@login_required(login_url='login')
def following_view(request):
    if request.user.is_authenticated:
        try:
            user_profile = Profile.objects.get(user=request.user)
        except Profile.DoesNotExist:
            user_profile = None

        if user_profile:
            user = request.user.username
            following_posts = Post.objects.filter(
                author__profile__in=user_profile.following.all()).exclude(author=request.user)
           
    tags = Tag.objects.all()
    popular_posts = Post.objects.annotate(num_likes=Count('likes')).order_by('-num_likes')[:3]
    context = {
       
        'user_profile': user_profile,
        'following_posts': following_posts,
        'tags': tags,
        'popular_posts': popular_posts
    }

    return render(request, 'blog/following.html', context)


def all_posts(request):
    q = request.GET.get('q', '').strip()
    tag = request.GET.get('tag', '')
    filter_param = request.GET.get('filter', '')
    all_posts = posts.all()
    filtered_posts_by_author = posts.filter(author__username__contains=q)
    filtered_posts_by_title = all_posts.filter(title__icontains=q)
    filtered_posts_by_tag = posts.filter(
        Q(tags__name__contains=q) | Q(tags__name=tag)).distinct()
    if q:
        filtered_posts = posts.filter(
            Q(tags__name=tag) |
            Q(tags__name__icontains=q) |
            Q(author__username__icontains=q) |
            Q(slug__icontains=q)
        ).distinct().order_by('-created_at', 'title')
    else:
        filtered_posts = None
    tag_posts = posts.filter(tags__name=tag)

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
    post = posts.get(slug=slug)
    user = request.user if request.user.is_authenticated else None
    form = None
    liked = Like.objects.filter(
        user=user, liked_post=post).exists()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = user
            comment.post_to_comment = post
            comment.save()
            post.comments.add(comment)
            user.profile.comments.add(comment)
            Notification.objects.create(recipient=post.author,
                                        actor = user,
                                        action= 'commented on your post: ',
                                        post =post,
                                        is_read = False,
                                        type='comment'
                                    
                                        )

            return redirect('post', slug=slug)

    else:
        form = CommentForm()

    if request.method == 'POST' and 'like' in request.POST:
        if request.user.is_authenticated:
            if not liked:
                like = Like.objects.create(
                    user=user, liked_post=post)
                post.likes.add(like)
                Notification.objects.create(recipient=post.author,
                                        actor = user,
                                        action= 'liked your post: ',
                                        post =post,
                                        is_read = False,
                                        type='like'
                                    
                                        )
                is_it_liked = True
            else:
                like = Like.objects.get(
                    user=user, liked_post=post)
                like.delete()
                post.likes.remove(like)
                is_it_liked = liked

            return redirect('post', slug=slug)
        else:
            return redirect('login')

    comments = post.comments.all()
    related_posts = posts.filter(tags__name__in=post.tags.values_list(
        'name', flat=True)).distinct().exclude(title=post.title).exclude(author=post.author)
    users_posts = posts.filter(author=post.author).exclude(title=post.title)

    context = {
        'post': post,
        'user': user,
        'form': form,
        'comments': comments,
        'related_posts': related_posts,
        'users_posts': users_posts,
        'is_it_liked': liked

    }
    return render(request, 'blog/post.html', context)


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


@login_required(login_url='login')
def deletePost(request, pk):
    post = posts.get(pk=pk)

    if request.method == "POST":
        post.delete()
        messages.info(request, 'Your post has been successfully deleted',
                      extra_tags='sucess-delete--post')
        return redirect('home')
    context = {
        'post': post,
        'id': id
    }
    return render(request, 'layout.html', context)


def deleteComment(request, pk):
    user = request.user.profile

    comment_to_delete = user.comments.get(pk=pk)
    redirect_url = request.POST.get('redirect_url', '/')

    if request.method == "POST":
        comment_to_delete.delete()

        user.comments.remove(comment_to_delete)
        messages.info(request, 'Your comment has been successfully deleted',
                      extra_tags='sucess-delete--post')
        return redirect(redirect_url)
    context = {
        'comment_to_delete':  comment_to_delete,
        'comment_id': pk
    }
    return render(request, 'components/delete2.html', context)


def editComment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    redirect_url = request.POST.get('redirect_url', '/')
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            messages.success(request, 'Comment successfuly edited')
            return redirect(redirect_url)
    else:
        form = CommentForm(instance=comment)
    context2 = {
        'comment_to_edit': comment,
        'form': form
    }

    return render(request, 'blog/components/commentFormModal.html', context2)


def editPost(request, id):
    post = posts.get(pk=id)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('new')
    else:
        form = PostForm(instance=post)

    context = {
        "form": form,
        "id": id
    }

    return render(request, 'blog/new.html', context)
