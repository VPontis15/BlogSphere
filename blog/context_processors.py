from .models import Navigation, Notification
from accounts.models import Profile


def render_Nav_processor(request):
  if request.user.is_authenticated:
    navigation_links = Navigation.objects.exclude(destination = 'login')
  else:
    navigation_links = Navigation.objects.exclude(destination = 'logout')
   
  
  
  return  {
        'nav_links': navigation_links,
    }


def render_Profile_processor(request):
  
  logged_user = request.user.profile  if request.user.is_authenticated else None

  notifications = Notification.objects.filter(recipient = request.user, is_read=False) if request.user.is_authenticated else None 

  return  {
        'logged_user': logged_user,
        'notifications': notifications
    }