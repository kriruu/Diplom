# Generated by Django 4.1.3 on 2023-02-19 19:55

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0007_rename_body_videobackhome_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videobackhome',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
    ]