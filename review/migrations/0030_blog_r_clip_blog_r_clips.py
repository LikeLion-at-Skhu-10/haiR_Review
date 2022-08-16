# Generated by Django 4.0.4 on 2022-08-15 07:32

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('review', '0029_alter_blog_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='r_clip',
            field=models.ManyToManyField(blank=True, related_name='r_clip', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='blog',
            name='r_clips',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
