# Generated by Django 4.2.7 on 2023-11-27 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='macllocmedia',
            name='months',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]