# Generated by Django 3.2 on 2021-04-27 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_aboutme_favorite_song'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(blank=True, default='x.png', null=True, upload_to='images'),
        ),
    ]
