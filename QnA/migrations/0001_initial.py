# Generated by Django 4.0.4 on 2022-07-26 07:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hashtag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='QnA',
            fields=[
                ('q_id', models.AutoField(primary_key=True, serialize=False)),
                ('question', models.CharField(max_length=200)),
                ('q_date', models.DateTimeField()),
                ('q_photo', models.ImageField(blank=True, upload_to='images/')),
                ('hashtags', models.ManyToManyField(blank=True, to='QnA.hashtag')),
            ],
        ),
        migrations.CreateModel(
            name='QnAComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=50)),
                ('qna_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='QnA.qna')),
            ],
        ),
    ]
