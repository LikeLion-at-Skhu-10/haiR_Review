# Generated by Django 4.1 on 2022-08-17 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_hashtag_p_id_hashtag_qna_id_hashtag_r_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review_gather',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('r_title', models.CharField(max_length=200)),
                ('r_body', models.TextField()),
            ],
        ),
    ]
