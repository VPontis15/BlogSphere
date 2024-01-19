from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.urls import reverse
from .forms import  UserForm, ChangingPasswordForm
from .models import Profile
from blog.models import Post
from accounts.helper import displayGreeting
from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm
from django.contrib.auth import update_session_auth_hash



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
               messages.success(request, f'{displayGreeting(request.user)}', extra_tags='login')
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
                messages.success(request,f"Welcome to Blogsphere {user.username}!",extra_tags='registration')
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

# @login_required(login_url='home')
# # def myProfile(request,tab):
#     pass
#     user_profile = Profile.objects.get(user=request.user)
#     my_posts = Post.objects.filter(author=request.user)

#     if request.method == "POST":
#         form = UserForm(request.POST, request.FILES, instance=user_profile)    
#         if form.is_valid():
#             form.save()
#             # url = reverse('my-profile')  
#             # url_with_params = f"{url}?tab={tab}"
#             messages.success(request, 'Profile updated successfully', extra_tags='update-profile')
#             return redirect('home')
#         else:
#             messages.error(request, 'Error updating profile. Please check the form.', extra_tags='update-profile')

#     else:
#         form = UserForm(instance=user_profile)

 

    

    # context ={
    #     'form': form,
    #     'tab': tab,
    #     'my_posts': my_posts,
    #     'user_profile': user_profile,
       
    # }

    # return render(request, 'account/myProfile.html', context)



# def change_user_password(request):
   
#     change_password_form = PasswordChangeForm(user=request.user,data= request.POST)
#     if change_password_form.is_valid():
#         change_password_form.save()
#         update_session_auth_hash(request, change_password_form.user)
#         return redirect('home')
#     return render(request, 'account/myProfile.html', {
#         'form': change_password_form,
        
#     })


def myΙnformations(request):

    user_profile = Profile.objects.get(user=request.user)
    if request.method == "POST":
        form = UserForm(request.POST, request.FILES, instance=user_profile)    
        if form.is_valid():
            form.save()
            # url = reverse('my-profile')  
            # url_with_params = f"{url}?tab={tab}"
            messages.success(request, 'Profile updated successfully', extra_tags='update-profile')
            return redirect('my-informations')
        else:
            messages.error(request, 'Error updating profile. Please check the form.', extra_tags='update-profile')

    else:
        form = UserForm(instance=user_profile)
    context={
        'form':form,
        'user_profile': user_profile
    }
    return render(request,'account/components/myProfile/form.html',context )

                                                  
def success(request):

    return render(request, 'components/success')