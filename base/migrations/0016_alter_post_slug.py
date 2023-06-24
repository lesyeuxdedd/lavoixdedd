# Generated by Django 4.1.9 on 2023-05-28 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0015_alter_post_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="slug",
            field=models.SlugField(
                blank=True, max_length=1024, null=True, verbose_name="Slug"
            ),
        ),
    ]