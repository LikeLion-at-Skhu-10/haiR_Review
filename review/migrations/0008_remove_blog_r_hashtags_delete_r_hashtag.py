# Generated by Django 4.0.6 on 2022-07-28 13:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0007_rename_hashtag_r_hashtag_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='r_hashtags',
        ),
        migrations.DeleteModel(
            name='r_Hashtag',
        ),
    ]