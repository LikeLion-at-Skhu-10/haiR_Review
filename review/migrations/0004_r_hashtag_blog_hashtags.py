from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0003_remove_blog_r_hashtag_delete_r_hashtag'),
    ]

    operations = [
        migrations.CreateModel(
            name='r_hashtag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='blog',
            name='hashtags',
            field=models.ManyToManyField(blank=True, to='review.r_hashtag'),
        ),
    ]