# Generated by Django 3.2.20 on 2023-08-25 12:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='content',
        ),
    ]
