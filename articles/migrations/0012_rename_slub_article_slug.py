# Generated by Django 3.2.20 on 2023-08-30 20:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0011_article_slub'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='slub',
            new_name='slug',
        ),
    ]
