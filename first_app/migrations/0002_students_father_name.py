# Generated by Django 4.2.7 on 2023-12-09 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='father_name',
            field=models.TextField(default='Lutfor Rahman'),
        ),
    ]