# Generated by Django 5.0 on 2024-01-12 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0020_rename_first_last_profile_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='following',
            field=models.ManyToManyField(related_name='followerss', to='accounts.profile'),
        ),
    ]