# Generated by Django 5.0.7 on 2024-08-27 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drinks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='drinks',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='drinks/'),
        ),
    ]
