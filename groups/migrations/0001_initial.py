
# Generated by Django 3.2.13 on 2022-12-08 06:09


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
            name="Group",
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
                ("title", models.CharField(max_length=200)),
                ("introduce", models.CharField(max_length=200)),
                ("place", models.CharField(max_length=200)),
                ("detail_place", models.CharField(default="모임장소", max_length=200)),
                ("meeting_date", models.DateField()),
                ("number", models.PositiveIntegerField()),
                ("end_date", models.DateField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("image", models.ImageField(upload_to="")),
                ("closed", models.BooleanField(default=False)),
                (
                    "like_user",
                    models.ManyToManyField(
                        related_name="like_group", to=settings.AUTH_USER_MODEL
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
