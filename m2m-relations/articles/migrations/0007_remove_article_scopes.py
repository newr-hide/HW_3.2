# Generated by Django 5.1.1 on 2024-10-03 05:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_article_scopes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='scopes',
        ),
    ]
