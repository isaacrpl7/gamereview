# Generated by Django 3.1.2 on 2020-10-29 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_auto_20201029_2122'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='id',
            field=models.AutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='review',
            name='number',
            field=models.IntegerField(default=0),
        ),
    ]