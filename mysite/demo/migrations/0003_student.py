# Generated by Django 4.2.7 on 2023-11-30 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0002_macllocmedia_months'),
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('mobile', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('message', models.CharField(max_length=15)),
            ],
        ),
    ]