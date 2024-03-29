# Generated by Django 5.0 on 2024-01-19 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_delete_follower'),
        ('blog', '0002_alter_post_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='comments',
            field=models.ManyToManyField(blank=True, related_name='user_comments', to='blog.comment'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], default='M', max_length=1, null=True),
        ),
    ]
