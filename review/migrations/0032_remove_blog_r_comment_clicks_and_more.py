# Generated by Django 4.0.4 on 2022-08-16 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0031_blog_r_comment_clicks'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='r_comment_clicks',
        ),
        migrations.AddField(
            model_name='r_comment',
            name='r_comment_clicks',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
