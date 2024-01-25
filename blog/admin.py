from django.contrib import admin
from .models import Post, Tag, Navigation, Comment, Like

# Register your models here.

admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Navigation)
admin.site.register(Like)
admin.site.register(Comment)
