# Generated by Django 4.0.4 on 2022-08-03 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0011_alter_blog_r_clicks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='r_clicks',
            field=models.PositiveIntegerField(default=0, verbose_name='조회수'),
        ),
    ]