# Generated by Django 4.1 on 2022-08-12 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("password", models.CharField(max_length=128, verbose_name="password")),
                ("username", models.CharField(max_length=20, unique=True)),
                ("name", models.CharField(max_length=20)),
                (
                    "email",
                    models.EmailField(
                        max_length=100, unique=True, verbose_name="email"
                    ),
                ),
                ("p_num", models.IntegerField(null=True)),
                (
                    "create_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="date joined"),
                ),
                (
                    "last_login",
                    models.DateTimeField(auto_now=True, verbose_name="last login"),
                ),
                ("is_admin", models.BooleanField(default=False)),
                ("is_active", models.BooleanField(default=True)),
                ("is_superuser", models.BooleanField(default=False)),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
