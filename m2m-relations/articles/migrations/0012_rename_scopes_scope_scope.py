# Generated by Django 5.1.1 on 2024-10-03 06:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0011_alter_scope_article'),
    ]

    operations = [
        migrations.RenameField(
            model_name='scope',
            old_name='scopes',
            new_name='scope',
        ),
    ]
