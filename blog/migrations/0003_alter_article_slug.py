# Generated by Django 5.0.3 on 2024-03-19 16:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0002_article_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="article",
            name="slug",
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]