# Generated by Django 5.0.6 on 2024-10-09 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='skills',
            name='aghs_icon',
            field=models.CharField(blank=True, max_length=2222, null=True),
        ),
    ]
