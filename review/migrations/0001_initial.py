# Generated by Django 4.0.6 on 2022-07-28 02:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('r_title', models.CharField(max_length=200)),
                ('r_body', models.TextField()),
                ('r_name', models.CharField(blank=True, max_length=20, null=True)),
                ('r_location', models.CharField(blank=True, max_length=20, null=True)),
                ('r_photo', models.ImageField(blank=True, upload_to='images/')),
                ('r_receipt', models.ImageField(blank=True, upload_to='images/')),
                ('r_nickname', models.CharField(blank=True, max_length=20, null=True)),
                ('r_clicks', models.PositiveIntegerField(default=1, verbose_name='조회수')),
                ('r_date', models.DateTimeField(verbose_name='data published')),
                ('r_likes', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Hashtag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='r_comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=20)),
                ('blog_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='review.blog')),
            ],
        ),
        migrations.AddField(
            model_name='blog',
            name='r_hashtag',
            field=models.ManyToManyField(blank=True, null=True, to='review.hashtag'),
        ),
    ]
