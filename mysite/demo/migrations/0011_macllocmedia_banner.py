# Generated by Django 4.2.7 on 2023-12-21 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0010_remove_macllocmedia_banner'),
    ]

    operations = [
        migrations.AddField(
            model_name='macllocmedia',
            name='banner',
            field=models.ImageField(default=12, upload_to='images/'),
            preserve_default=False,
        ),
    ]
