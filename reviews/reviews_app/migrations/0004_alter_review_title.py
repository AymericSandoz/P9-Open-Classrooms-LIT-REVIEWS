# Generated by Django 4.2.6 on 2024-01-04 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews_app', '0003_remove_blog_author_remove_blog_photo_delete_revue_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='title',
            field=models.CharField(max_length=128),
        ),
    ]
