# Generated by Django 4.1.3 on 2023-02-19 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0002_alter_videobackhome_content_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videobackhome',
            name='videofile',
            field=models.FileField(null=True, upload_to='static/video/'),
        ),
    ]
