# Generated by Django 4.2.7 on 2023-12-01 13:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0004_alter_macllocmedia_contain'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='macllocmedia',
            name='btn',
        ),
    ]