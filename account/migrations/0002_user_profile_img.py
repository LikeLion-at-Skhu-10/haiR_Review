# Generated by Django 4.1 on 2022-08-12 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="profile_Img",
            field=models.ImageField(blank=True, upload_to="images/"),
        ),
    ]
