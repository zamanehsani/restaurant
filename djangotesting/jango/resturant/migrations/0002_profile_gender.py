# Generated by Django 3.1.1 on 2020-11-15 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resturant', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('m', 'male'), ('f', 'female'), ('other', 'other')], max_length=50, null=True),
        ),
    ]