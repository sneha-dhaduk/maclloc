# Generated by Django 4.2.7 on 2024-01-19 13:31

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0015_studentreview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='mobile',
            field=models.IntegerField(default='1234567890', max_length=10, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:\\d+)*\\Z'), code='invalid', message=None), django.core.validators.MinLengthValidator(10)]),
        ),
    ]