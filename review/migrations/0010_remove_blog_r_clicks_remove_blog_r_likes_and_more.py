# Generated by Django 4.0.6 on 2022-08-11 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0009_hashtag_blog_hashtags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='r_clicks',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='r_likes',
        ),
        migrations.AddField(
            model_name='blog',
            name='r_clikes',
            field=models.IntegerField(default=0),
        ),
    ]
