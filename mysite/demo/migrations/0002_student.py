# Generated by Django 5.0.1 on 2024-02-05 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('rollno', models.IntegerField()),
                ('branch', models.CharField(max_length=10)),
            ],
        ),
    ]
