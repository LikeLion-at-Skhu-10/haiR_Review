# Generated by Django 4.1 on 2022-08-12 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0001_initial"),
        ("free", "0001_initial"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Hashtag",
        ),
        migrations.AlterField(
            model_name="free",
            name="hashtags",
            field=models.ManyToManyField(blank=True, null=True, to="main.hashtag"),
        ),
    ]
