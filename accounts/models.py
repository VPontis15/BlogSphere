from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from .helper import default_date

# Create your models here.
class Profile(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    OTHER = 'O'

    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER, 'Other'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True,null=True,  max_length = 400)
    profile_pic = models.ImageField( blank=True, null=True)
    gender = models.CharField(null=True,  max_length=1,choices=GENDER_CHOICES, default= MALE)
    birthday = models.DateField(null=True, blank = True, default=default_date)
    job = models.CharField(blank=True, null=True,  max_length = 400)
    full_name = models.CharField(null=True, max_length = 200, blank= True)
    country = models.CharField(null=True, blank=True, max_length=100)
    city = models.CharField(null=True, blank=True, max_length=100)
    following = models.ManyToManyField('self')
    followers = models.ManyToManyField("self", related_name="followed_by", symmetrical=False, blank=True)


    def __str__(self):
        return f"{self.user.username}"
    


def create_profile(sender, instance, created, **kwargs):
     if created:
        user_profile = Profile(user=instance)
        user_profile.save()
        # user_profile.followers.set([instance.profile.id])

post_save.connect(create_profile, sender=User)

