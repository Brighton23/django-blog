# Generated by Django 1.10.5 on 2017-01-25 11:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("djangocms_blog", "0026_merge"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="date_featured",
            field=models.DateTimeField(blank=True, null=True, verbose_name="featured date"),
        ),
    ]