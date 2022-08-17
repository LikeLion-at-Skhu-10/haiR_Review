# Generated by Django 4.1 on 2022-08-12 06:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Free",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("p_title", models.CharField(max_length=200)),
                ("p_date", models.DateTimeField(verbose_name="data published")),
                ("p_body", models.TextField()),
                ("p_photo", models.ImageField(blank=True, upload_to="images/")),
                ("p_likes", models.CharField(blank=True, max_length=20, null=True)),
                (
                    "p_clicks",
                    models.PositiveIntegerField(default=1, verbose_name="조회수"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Hashtag",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="p_comment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("text", models.CharField(max_length=20)),
                (
                    "p_id",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="p_comments",
                        to="free.free",
                    ),
                ),
                (
                    "pc_writer",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="free",
            name="hashtags",
            field=models.ManyToManyField(blank=True, null=True, to="free.hashtag"),
        ),
        migrations.AddField(
            model_name="free",
            name="name",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
