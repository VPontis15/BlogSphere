from django.db import models
from django.db.models.signals import post_save #Import a post_save signal when a user is created
from django.contrib.auth.models import User # Import the built-in User model, which is a sender
from django.dispatch import receiver # Import the receiver

# Create your models here.


class UserProfile(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    OTHER = 'O'

    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER, 'Other'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.CharField(max_length = 100, null=True, blank= True)
    birthday=models.DateField(auto_now=False, null=True, blank=True)
    gender = models.CharField(null=True,  max_length=1,choices=GENDER_CHOICES, default= MALE)
    profile_pic = models.ImageField( blank=True, null=True)
    country = models.CharField( max_length=150)
    city = models.CharField(max_length = 100)
    full_name = models.CharField(max_length = 200)
    followers = models.ManyToManyField("self")
    following = models.ManyToManyField('self')

    def save(self, *args, **kwargs):
        self.full_name = f"{self.first_name} {self.last_name}"
        super().save(*args, **kwargs)



