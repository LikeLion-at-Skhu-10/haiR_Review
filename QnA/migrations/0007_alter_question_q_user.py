# Generated by Django 4.0.4 on 2022-08-19 11:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('QnA', '0006_question_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='q_user',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='q_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
