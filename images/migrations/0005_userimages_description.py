# Generated by Django 3.2.8 on 2021-11-05 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0004_usermodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='userimages',
            name='description',
            field=models.TextField(default='unknow'),
        ),
    ]
