# Generated by Django 4.0.6 on 2022-07-27 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('free', '0003_blog_p_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='p_clicks',
            field=models.PositiveIntegerField(default=1, verbose_name='조회수'),
        ),
    ]
