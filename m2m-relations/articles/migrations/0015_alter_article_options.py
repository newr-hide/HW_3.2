# Generated by Django 5.1.1 on 2024-10-03 08:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0014_alter_scope_options_alter_scope_is_main_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-published_at'], 'verbose_name': 'Статья', 'verbose_name_plural': 'Статьи'},
        ),
    ]
