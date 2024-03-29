# Generated by Django 5.0 on 2024-01-18 13:47

import accounts.helper
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blog', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, max_length=400, null=True)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], default='M', max_length=1, null=True)),
                ('birthday', models.DateField(blank=True, default=accounts.helper.default_date, null=True)),
                ('job', models.CharField(blank=True, max_length=400, null=True)),
                ('first_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('full_name', models.CharField(blank=True, max_length=200, null=True)),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('comments', models.ManyToManyField(related_name='user_comments', to='blog.comment')),
                ('followers', models.ManyToManyField(blank=True, related_name='followed_by', to='accounts.profile')),
                ('following', models.ManyToManyField(blank=True, to='accounts.profile')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
