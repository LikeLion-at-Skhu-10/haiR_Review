# Generated by Django 4.0.4 on 2022-08-19 08:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('free', '0008_delete_free_clicks'),
    ]

    operations = [
        migrations.RenameField(
            model_name='free',
            old_name='user',
            new_name='p_user',
        ),
    ]