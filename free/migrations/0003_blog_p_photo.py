# Generated by Django 4.0.6 on 2022-07-27 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('free', '0002_rename_body_blog_p_body_rename_pub_date_blog_p_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='p_photo',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
