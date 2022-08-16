# Generated by Django 4.0.4 on 2022-08-13 12:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like_count', models.PositiveIntegerField(default=0)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.profile')),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='like_post',
            field=models.ManyToManyField(blank=True, related_name='like_users', to='account.post'),
        ),
    ]
