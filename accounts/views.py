from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .forms import  UserForm
from .models import Profile
from blog.models import Post


# Create your views here.


def loginPage(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
           username = form.cleaned_data.get('username')
           password = form.cleaned_data.get('password')
           user = authenticate(username=username, password= password)
           if user is not None:
               login(request, user)
              
               return redirect('home')
           else:
               messages.error(request,'Wrong inputs')
               return redirect('login')
    else:
        form = AuthenticationForm()
   
    return render(request, 'account/login.html', {'form': form })

def logoutPage(request):
    logout(request)
    return redirect('login')


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            if User.objects.filter(username = username).exists() or User.objects.filter(email = email).exists():
                messages.error(request, 'User already exist')
                return redirect('register')
            else:
                user = form.save()
                messages.success(request,f"Welcome to Blogsphere! {user.username}")
                login(request,user)
                return redirect('home') 
        else:
                messages.error(request, 'An error occured during registration')
                return redirect('register')     
    else:
        form = UserCreationForm()
    return render(request, 'account/register.html', {"form": form})



def viewProfile(request, username, tab):
    user_profile = Profile.objects.get(user__username=username)
    is_users_profile = user_profile.user == request.user
    user_posts = Post.objects.filter(author__username = username )

    

    context = {
        "user_profile": user_profile,
        "tab": tab,
        "is_users_profile": is_users_profile,
        "user_posts": user_posts
    }
    return render(request, "account/user-profile.html", context)


def EditProfile(request):
     user_profile = Profile.objects.get(user = request.user)
     user = User.objects.get(id = request.user.id)
     if request.method == "POST":
        form = UserForm(request.POST, instance=user_profile)
        if form.is_valid():
            user_profile.first_name = form.cleaned_data['first_name']
            user_profile.last_name = form.cleaned_data['last_name']
            user_profile.email = form.cleaned_data['email']

            # Save both the User and Profile instances
            user.save()
            user_profile.save()

            messages.success(request, 'Profile updated successfully')
            return redirect('home')  
        else:
            messages.error(request, 'Something went wrong')
     else:
        form = UserForm(instance=user_profile)
        
     
     context ={
         'form': form,
         "user_profile": user_profile
     }

     return render(request, 'account/myProfile.html', context)



                                                  
def success(request):

    return render(request, 'components/success')