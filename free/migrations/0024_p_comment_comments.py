# Generated by Django 4.0.4 on 2022-08-16 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('free', '0023_rename_like_blog_f_like_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='p_comment',
            name='comments',
            field=models.PositiveIntegerField(null=True, verbose_name='댓글수'),
        ),
    ]
