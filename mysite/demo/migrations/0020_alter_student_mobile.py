# Generated by Django 4.2.7 on 2024-01-19 15:09

import demo.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0019_alter_student_mobile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='mobile',
            field=models.CharField(max_length=10, validators=[demo.models.validate_ten_digit]),
        ),
    ]
