# Generated by Django 3.2.13 on 2022-08-19 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('free', '0003_auto_20220818_0134'),
    ]

    operations = [
        migrations.AddField(
            model_name='free',
            name='p_clicks',
            field=models.PositiveIntegerField(default=0, verbose_name='조회수'),
        ),
    ]
