# Generated by Django 4.0.4 on 2022-08-16 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0030_blog_r_clip_blog_r_clips'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='r_comment_clicks',
            field=models.PositiveIntegerField(default=0),
        ),
    ]