from .models import Navigation

def render_Nav_processor(request):
  if request.user.is_authenticated:
    navigation_links = Navigation.objects.exclude(destination = 'login')
  else:
    navigation_links = Navigation.objects.exclude(destination = 'logout').exclude(destination = 'editProfile')
   
      
  
  return  {
        'nav_links': navigation_links
    }