# Generated by Django 3.0.4 on 2020-04-12 10:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0004_auto_20200412_1214'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='feedback',
            unique_together={('movie', 'rating', 'discuss')},
        ),
    ]
