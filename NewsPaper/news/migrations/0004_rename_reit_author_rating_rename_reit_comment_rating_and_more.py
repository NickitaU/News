# Generated by Django 5.1.4 on 2024-12-19 12:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_alter_comment_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='reit',
            new_name='rating',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='reit',
            new_name='rating',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='reit',
            new_name='rating',
        ),
    ]
