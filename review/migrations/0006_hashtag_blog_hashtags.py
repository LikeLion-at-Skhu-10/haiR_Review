from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0005_remove_blog_hashtags_delete_r_hashtag'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hashtag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='blog',
            name='hashtags',
            field=models.ManyToManyField(blank=True, null=True, to='review.hashtag'),
        ),
    ]