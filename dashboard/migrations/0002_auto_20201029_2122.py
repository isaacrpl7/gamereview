# Generated by Django 3.1.2 on 2020-10-29 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='release_date',
            field=models.CharField(max_length=100),
        ),
    ]
