# Generated by Django 4.2.7 on 2023-12-09 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0005_remove_macllocmedia_btn'),
    ]

    operations = [
        migrations.AddField(
            model_name='macllocmedia',
            name='image1',
            field=models.ImageField(default=1, upload_to='images/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='macllocmedia',
            name='title',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
