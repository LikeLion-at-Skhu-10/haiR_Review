# Generated by Django 4.1 on 2022-08-18 14:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('QnA', '0004_alter_question_q_likes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='q_clips',
            new_name='q_clicks',
        ),
    ]
