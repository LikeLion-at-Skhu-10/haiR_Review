from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0004_r_hashtag_blog_hashtags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='hashtags',
        ),
        migrations.DeleteModel(
            name='r_hashtag',
        ),
    ]