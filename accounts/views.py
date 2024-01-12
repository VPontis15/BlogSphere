from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .forms import UserForm


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
    username = User.objects.get(username = username)
    if request.method == "POST":
        form = UserForm(request.POST,instance= username)
        form.save()
    else:
        form = UserForm(instance=username)
    context = {
        "username": username,
        "form": form,
        "tab": tab
    }
    return render(request, "account/user-profile.html", context)





                                                  
def success(request):

    return render(request, 'components/success')