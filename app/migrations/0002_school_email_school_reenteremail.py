# Generated by Django 4.2.7 on 2024-01-09 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='email',
            field=models.EmailField(default=1, max_length=254, verbose_name='default=some@gmail.com'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='school',
            name='reenteremail',
            field=models.EmailField(default=2, max_length=254, verbose_name='default=some@gmail.com'),
            preserve_default=False,
        ),
    ]
