# Generated by Django 4.1.7 on 2023-03-22 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cakeapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cakes',
            name='profile',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
