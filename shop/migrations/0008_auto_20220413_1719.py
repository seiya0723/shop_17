# Generated by Django 3.2.12 on 2022-04-13 08:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_auto_20220413_1039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='color',
            field=models.CharField(blank=True, max_length=7, null=True, validators=[django.core.validators.RegexValidator(regex='^#(?:[0-9a-f]{6})$')], verbose_name='色'),
        ),
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.CharField(blank=True, choices=[('S', 'S'), ('M', 'M'), ('L', 'L'), ('LL', 'LL'), ('XL', 'XL')], max_length=2, null=True, verbose_name='サイズ'),
        ),
    ]
