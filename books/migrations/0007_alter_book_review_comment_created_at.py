# Generated by Django 3.2.13 on 2022-12-01 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_auto_20221201_1007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book_review_comment',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
