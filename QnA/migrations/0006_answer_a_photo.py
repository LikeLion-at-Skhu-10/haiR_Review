# Generated by Django 4.1 on 2022-08-14 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("QnA", "0005_alter_answer_text_alter_question_question"),
    ]

    operations = [
        migrations.AddField(
            model_name="answer",
            name="a_photo",
            field=models.ImageField(blank=True, null=True, upload_to="a_images/"),
        ),
    ]
