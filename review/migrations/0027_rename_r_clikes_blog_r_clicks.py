# Generated by Django 4.0.4 on 2022-08-11 11:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0026_blog_r_clikes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='r_clikes',
            new_name='r_clicks',
        ),
    ]
