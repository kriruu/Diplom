# Generated by Django 4.1.3 on 2023-02-19 23:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0010_category_infoforall'),
    ]

    operations = [
        migrations.RenameField(
            model_name='videobackhome',
            old_name='content',
            new_name='Video_content',
        ),
        migrations.RenameField(
            model_name='videobackhome',
            old_name='is_published',
            new_name='Video_is_published',
        ),
        migrations.RenameField(
            model_name='videobackhome',
            old_name='title',
            new_name='Video_title',
        ),
    ]