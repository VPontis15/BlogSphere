from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'


class Navigation(models.Model):
    text = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)

    def __str__(self):
        return f"Text={self.text}, Destination = {self.destination}"


class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User,  on_delete=models.CASCADE)
    body = RichTextUploadingField(blank=True, null=True)
    created_at = models.DateField(auto_now=True)
    tags = models.ManyToManyField(Tag)
    slug = models.SlugField(unique=True, editable=False,
                            blank=True, db_index=True, default='')
    comments = models.ManyToManyField('Comment', blank=True)
    likes = models.ManyToManyField('Like', blank=True)

    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):

        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Title = {self.title} Author = {self.author} Content = {self.body[:50]} Date = {self.created_at} Tags = {self.tags}"


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_to_comment = models.ForeignKey(Post, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now)
    body = models.TextField()

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f"User: {self.user} commented  {self.body} on {self. post_to_comment.title} "


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    liked_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now)


def __str__(self):
    return f'{self.user.username} liked {self.content_object}'
