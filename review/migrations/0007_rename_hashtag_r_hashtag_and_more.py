from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0006_hashtag_blog_hashtags'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Hashtag',
            new_name='r_Hashtag',
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='hashtags',
            new_name='r_hashtags',
        ),
    ]
