# Generated by Django 4.1.3 on 2023-02-19 19:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0006_rename_content_videobackhome_body'),
    ]

    operations = [
        migrations.RenameField(
            model_name='videobackhome',
            old_name='body',
            new_name='content',
        ),
    ]