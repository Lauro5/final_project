# Generated by Django 3.2.5 on 2022-12-17 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='slug',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
